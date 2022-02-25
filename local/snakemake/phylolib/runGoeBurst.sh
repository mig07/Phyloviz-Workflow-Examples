#!/bin/bash

rm -rf .results
snakemake -c4 -s goeburst_hamming_lbr.py Hamming GoeBurst Lbr
