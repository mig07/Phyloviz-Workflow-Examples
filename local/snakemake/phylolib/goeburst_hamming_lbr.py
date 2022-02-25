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

rule GoeBurst:
    input:
        matrix=".results/matrix.txt"
    output:
        tree=".results/tree.txt"
    shell:
        """
        java -jar ../../../res/phylolib/jar/*.jar \
        algorithm goeburst --out=newick:{output.tree} --matrix=symmetric:{input.matrix}
        """

rule Lbr:
    input:
        matrix=".results/matrix.txt",
        tree=".results/tree.txt",
        dataset="../../../res/phylolib/data/datasets/10.txt"
    output:
        out=".results/out.txt"
    shell:
        """
        java -jar ../../../res/phylolib/jar/*.jar \
        optimization lbr --tree=newick:{input.tree} --dataset=ml:{input.dataset} --matrix=symmetric:{input.matrix} --out=newick:{output.out}
        """
