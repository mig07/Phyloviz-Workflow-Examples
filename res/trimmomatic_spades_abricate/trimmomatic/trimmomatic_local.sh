java -jar trimmomatic.jar \
    PE -phred33 \
    ~/Desktop/ERR406040.fastq \
    ~/Desktop/ERR406040.fastq \
    ERR406040.trimmed.fastq ERR406040.untrimmed.fastq ERR406040.trimmed.fastq ERR406040.untrimmed.fastq  \
    LEADING:3 TRAILING:3 SLIDINGWINDOW:4:20 MINLEN:36
