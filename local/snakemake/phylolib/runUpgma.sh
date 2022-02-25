#!/bin/bash

rm -rf .results
snakemake -c4 -s upgma_hamming.py Hamming Upgma
