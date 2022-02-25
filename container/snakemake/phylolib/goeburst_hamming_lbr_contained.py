rule Hamming:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        distance hamming --dataset=ml:data/datasets/10.txt --out=symmetric:matrix.txt
        """

rule GoeBurst:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        algorithm goeburst --out=newick:tree.txt --matrix=symmetric:matrix.txt
        """

rule Lbr:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        optimization lbr --tree=newick:tree.txt --dataset=ml:data/datasets/10.txt --matrix=symmetric:matrix.txt --out=newick:out.txt
        """
