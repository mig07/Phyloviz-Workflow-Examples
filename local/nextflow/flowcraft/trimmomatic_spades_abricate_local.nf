#!/usr/bin/env nextflow

params.saveMode = 'copy'
params.filePattern = '/home/miguel/Desktop/ERR406040.fastq'
params.resultsDir = '.results'

Channel.fromFilePairs(params.filePattern)
        .set { ch_in_trimmomatic }

process trimmomatic {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    path 'fastqIn' from params.filePattern

    output:
    tuple path(fq_1_paired), path(fq_1_unpaired) into ch_out_trimmomatic

    script:

    fq_1_paired = 'ERR406040_trimmed.fastq'
    fq_1_unpaired = 'ERR406040_untrimmed.fastq'

    '''
    java -jar /home/miguel/Repo/ISEL/TFM83/Script/nextflow/flowcraft_pipeline/trimmomatic/trimmomatic.jar \
    PE -phred33 \
    fastqIn \
    fastqIn \
    ERR406040_trimmed.fastq \
    ERR406040_untrimmed.fastq \
    ERR406040_trimmed.fastq \
    ERR406040_untrimmed.fastq \
    LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36
    '''
}

process spades {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    tuple path(fq_1_paired), path(fq_1_unpaired) from ch_out_trimmomatic

    output:
    path """ERR406040.fasta""" into ch_out_spades

    script:

    '''
    spades.py -k 21,33,55,77 \
    --careful --only-assembler --pe1-1 \
    ${ERR406040.fasta} \
    --pe1-2 ${ERR406040.fasta} \
    -o ${ERR406040.fasta} -t 2 \
    cp ERR406040.fasta ERR406040.fasta
    '''
}
