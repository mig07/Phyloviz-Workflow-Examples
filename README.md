# Phyloviz-Workflow-Examples
Pipeline examples for airflow, nextflow and snakemake workflow systems

This repository has the following general directory tree:

```
.
├── container
│   ├── airflow
│   ├── nextflow
│   ├── shell
│   └── snakemake
├── local
│   ├── airflow
│   ├── nextflow
│   ├── shell
│   └── snakemake
└── res
    ├── phylolib
    └── trimmomatic
```

There are 3 main folders:

- **container** - Every pipeline that executes inside containers (requirements: docker and singularity);

- **local** - Every pipeline that executes locally (there are requirements specific to each pipeline);

- **res** - All resources needed to run each pipeline, either local or containerized ones.

Each pipeline folder has its own readme to provide guidance in its execution.
