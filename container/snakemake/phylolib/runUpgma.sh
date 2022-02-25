#!/bin/bash

rm -rf .results
snakemake -c4 -s upgma_hamming_contained.py Hamming Upgma
