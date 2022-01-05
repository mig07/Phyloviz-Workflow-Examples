rule all:
    input:
        "abricate_result.csv"

rule Trimmomatic:
    shell:
        """
        docker run -v $HOME/.fastqTest:/fastq --workdir /fastq trimmomatic:latest \
        java -jar /NGStools/Trimmomatic-0.39/trimmomatic.jar \
        PE -phred33 \
        /fastq/sample1_1.fastq \
        /fastq/sample1_2.fastq \
        sample1_R1_trimmed.fastq \
        sample1_R1_untrimmed.fastq \
        sample1_R2_trimmed.fastq \
        sample1_R2_untrimmed.fastq \
        ILLUMINACLIP:/NGStools/Trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10
        """

rule Spades:
    shell:
        """
        docker run -v $HOME/.fastqTest:/fastq --workdir /fastq spades:latest \
        /NGStools/SPAdes-3.14.0-Linux/bin/spades.py -k 21,33,55,77 \
        --careful --only-assembler \
        --pe1-1 /fastq/sample1_R1_trimmed.fastq \
        --pe1-2 /fastq/sample1_R2_trimmed.fastq \
        -o fq_spades.fasta \
        """

rule Abricate:
    output:
        abricate_result='abricate_result.csv'
    shell:
        """
        docker run -v $HOME/.fastqTest:/fastq --workdir /fastq abricate:latest \
        abricate /fastq/fq_spades.fasta/contigs.fasta --db card --csv > abricate_result.csv
        """
