from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.docker.operators.docker import DockerOperator

from docker.types import Mount

default_args = {
    'owner'                 : 'airflow',
    'description'           : 'Hamming -> Upgma pipeline from phylolib',
    'depend_on_past'        : False,
    'start_date'            : datetime(2022, 2, 21),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    'retries'               : 1,
    'retry_delay'           : timedelta(minutes=5)
}

with DAG('Hamming-Upgma-DockerOperators', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:

    hamming = DockerOperator(
        task_id='hamming',
        image='phylolib:latest',
        api_version='auto',
        mounts=[Mount(target='/phylolib', source='/opt/.phylolibVol', type='bind')],
        command='distance hamming --dataset=ml:/phylolib/data/datasets/10.txt --out=symmetric:/phylolib/out.txt',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

    upgma = DockerOperator(
        task_id='upgma',
        image='phylolib:latest',
        api_version='auto',
        mounts=[Mount(target='/phylolib', source='/opt/.phylolibVol', type='bind')],
        command='algorithm upgma --out=newick:/phylolib/tree.txt --matrix=symmetric:/phylolib/out.txt',
        auto_remove=True,
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
    )

hamming >> upgma
