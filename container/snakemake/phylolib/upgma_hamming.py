rule Hamming:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        distance hamming --dataset=ml:data/datasets/10.txt --out=symmetric:matrix.txt        
        """

rule Upgma:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        algorithm upgma --out=newick:tree.txt --matrix=symmetric:matrix.txt        
        """