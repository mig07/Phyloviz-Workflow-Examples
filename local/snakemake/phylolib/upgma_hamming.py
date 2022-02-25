rule Hamming:
    input:
        dataset="../../../res/phylolib/data/datasets/10.txt"
    output:
        matrix=".results/matrix.txt"
    shell:
        """
        java -jar ../../../res/phylolib/jar/*.jar \
        distance hamming --dataset=ml:{input.dataset} --out=symmetric:{output.matrix}
        """

rule Upgma:
    input:
        matrix=".results/matrix.txt"
    output:
        tree=".results/tree.txt"
    shell:
        """
        java -jar ../../../res/phylolib/jar/*.jar \
        algorithm upgma --out=newick:{output.tree} --matrix=symmetric:{input.matrix}
        """
