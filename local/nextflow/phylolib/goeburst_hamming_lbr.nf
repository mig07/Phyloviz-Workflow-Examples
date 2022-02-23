#!/usr/bin/env nextflow

params.saveMode = 'copy'
params.filePattern = '../../../res/phylolib'
params.resultsDir = '.results'

Channel.fromPath(params.filePattern)
        .set { ch_in_hamming }

process hamming {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    file 'resources' from ch_in_hamming

    output:
    path(matrix) into ch_out_hamming

    script:
    matrix='matrix.txt'

    '''
    java -jar resources/jar/*.jar distance hamming --dataset=ml:resources/data/datasets/10.txt --out=symmetric:matrix.txt
    '''
}

Channel.fromPath(params.filePattern)
        .set { ch_in_goeburst }

process goeburst {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    file 'resources' from ch_in_goeburst
    file 'matrix.txt' from ch_out_hamming

    output:
    tuple path(tree), path(matrix) into ch_out_goeburst

    script:
    tree='tree.txt'
    matrix='matrix.txt'

    '''
    java -jar resources/jar/*.jar algorithm goeburst --out=newick:tree.txt --matrix=symmetric:matrix.txt
    '''
}

Channel.fromPath(params.filePattern)
        .set { ch_in_lbr }

process lbrOptimization {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    file 'resources' from ch_in_lbr
    tuple path(tree), path(matrix) from ch_out_goeburst

    output:
    path(out) into ch_out_lbr

    script:
    out='out.txt'

    '''
    java -jar resources/jar/*.jar optimization lbr --tree=newick:tree.txt --dataset=ml:resources/data/datasets/10.txt --matrix=symmetric:matrix.txt --out=newick:out.txt
    '''
}