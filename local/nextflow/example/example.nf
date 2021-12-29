#!/usr/bin/env nextflow

params.str = 'Hello world!'
params.outputDir = "${baseDir}/output"

process splitLetters {

    output:
    file 'chunk_*' into letters

    """
    printf '${params.str}' | split -b 6 - chunk_
    """
}


process convertToUpper {

    publishDir params.outputDir

    input:
    file x from letters.flatten()

    output:
    file 'out.txt' into results

    """
    cat $x | tr '[a-z]' '[A-Z]' >out.txt
    """
}

results.view { it.trim() }
