from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.operators.bash import BashOperator

from docker.types import Mount

default_args = {
    'owner'                 : 'airflow',
    'description'           : 'Trimmomatic -> Spades -> Pilon -> Fork(Prokka, Abricate) example pipeline',
    'depend_on_past'        : False,
    'start_date'            : datetime(2022, 2, 21),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}

with DAG('Trimmomatic-Spades-Pilon-Prokka_Abricate-DockerOperators', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:

    trimmomatic = DockerOperator(
        task_id='trimmomatic',
        image='trimmomatic:latest',
        api_version='auto',
        mounts=[Mount(target='/fastq', source='/opt/.fastqTest', type='bind')],
        command='java -jar /NGStools/Trimmomatic-0.39/trimmomatic.jar \
                PE -phred33 \
                /fastq/sample1_1.fastq \
                /fastq/sample1_2.fastq \
                /fastq/sample1_R1_trimmed.fastq \
                /fastq/sample1_R1_untrimmed.fastq \
                /fastq/sample1_R2_trimmed.fastq \
                /fastq/sample1_R2_untrimmed.fastq \
                ILLUMINACLIP:/NGStools/Trimmomatic-0.39/adapters/TruSeq3-SE.fa:2:30:10',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    spades = DockerOperator(
        task_id='spades',
        image='spades:latest',
        api_version='auto',
        mounts=[Mount(target='/fastq', source='/opt/.fastqTest', type='bind')],
        command='/NGStools/SPAdes-3.14.0-Linux/bin/spades.py -k 21,33,55,77 --careful --only-assembler \
                --pe1-1 /fastq/sample1_R1_trimmed.fastq \
                --pe1-2 /fastq/sample1_R2_trimmed.fastq \
                -o /fastq/fq_spades.fasta',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    #pilon = DockerOperator(
        #task_id='pilon',
        #image='pilon:latest',
        #api_version='auto',
        #mounts=[Mount(target='/fastq', source='/opt/.fastqTest', type='bind')],
        #command='java -jar pilon-1.22.jar --genome /fastq/fq_spades.fasta/contigs.fasta --output pilonOuts',
        #auto_remove=True,
        #docker_url='unix://var/run/docker.sock',
        #network_mode='bridge'
    #)

    pilon = BashOperator(
        task_id='pilon',
        bash_command='sleep 2',
    )

    prokka = BashOperator(
        task_id='prokka',
        bash_command='sleep 2',
    )

    abricate = DockerOperator(
        task_id='abricate',
        image='abricate:latest',
        api_version='auto',
        mounts=[Mount(target='/fastq', source='/opt/.fastqTest', type='bind')],
        command='abricate /fastq/fq_spades.fasta/contigs.fasta --db card --csv',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

trimmomatic >> spades >> pilon >> [prokka, abricate]
