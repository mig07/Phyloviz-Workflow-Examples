#!/usr/bin/env nextflow

params.saveMode = 'copy'
params.filePattern = '../../../res/trimmomatic_spades_abricate/fastq/*_{1,2}.fastq'
params.resultsDir = '.results'

Channel.fromPath(params.filePattern)
        .set { ch_in_trimmomatic }

process trimmomatic {
    container 'trimmomatic:latest'

    input:
    file 'inFastq' from ch_in_trimmomatic

    output:
    tuple path(fq_1_trimmed), path(fq_2_trimmed) into ch_out_trimmomatic

    script:

    fq_1_trimmed = 'sample1_R1_trimmed.fastq'
    fq_1_untrimmed = 'sample1_R1_untrimmed.fastq'
    fq_2_trimmed = 'sample1_R2_trimmed.fastq'
    fq_2_untrimmed = 'sample1_R2_untrimmed.fastq'

    '''
    java -jar /NGStools/Trimmomatic-0.39/trimmomatic.jar \
    PE -phred33 \
    inFastq \
    inFastq \
    sample1_R1_trimmed.fastq \
    sample1_R1_untrimmed.fastq \
    sample1_R2_trimmed.fastq \
    sample1_R2_untrimmed.fastq \
    ILLUMINACLIP:/NGStools/Trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10
    '''
}

process spades {
    container 'spades:latest'

    input:
    tuple 'fq_1_paired.fastq', 'fq_2_paired.fastq' from ch_out_trimmomatic

    output:
    path 'fq_spades.fasta' into ch_out_spades

    script:
    '''
    /NGStools/SPAdes-3.14.0-Linux/bin/spades.py -k 21,33,55,77 \
    --careful --only-assembler \
    --pe1-1 fq_1_paired.fastq \
    --pe1-2 fq_2_paired.fastq \
    -o fq_spades.fasta \
    '''
}

process pilon {
    container 'trimmomatic:latest'
    input:
        path 'fq_spades.fasta' from ch_out_spades
    output:
        path 'fq_spades.fasta' into ch_out_pilon1
        path 'fq_spades.fasta' into ch_out_pilon2
    script:
    '''
    echo test
    '''
}

process prokka {
    container 'trimmomatic:latest'
    input:
        path 'fq_spades.fasta' from ch_out_pilon1
    output:

    script:
    '''
    echo test
    '''
}

process abricate {
    container 'abricate:latest'
    publishDir params.resultsDir, mode: params.saveMode

    input:
    path 'fq_spades.fasta' from ch_out_pilon2

    output:
    path 'abricate_result.csv' into ch_out_abricate

    script:
    '''
    abricate fq_spades.fasta/contigs.fasta --db card --csv > abricate_result.csv
    '''
}
