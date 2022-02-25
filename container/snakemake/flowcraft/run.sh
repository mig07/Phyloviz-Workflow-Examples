#!/bin/bash

rm -rf abricate_result.csv
snakemake -c4 -s trimmomatic_spades_abricate_contained.py Trimmomatic Spades Abricate
