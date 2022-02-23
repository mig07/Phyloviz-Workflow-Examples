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
    path(out) into ch_out_hamming

    script:
    out='out.txt'

    '''
    java -jar /app.jar distance hamming --dataset=ml:resources/data/datasets/10.txt --out=symmetric:out.txt
    '''
}

Channel.fromPath(params.filePattern)
        .set { ch_in_upgma }

process upgma {
    publishDir params.resultsDir, mode: params.saveMode

    input:
    file 'resources' from ch_in_upgma
    file 'out.txt' from ch_out_hamming

    output:
    path(tree) into ch_out_upgma

    script:
    tree='tree.txt'

    '''
    java -jar /app.jar algorithm upgma --out=newick:tree.txt --matrix=symmetric:out.txt
    '''
}
