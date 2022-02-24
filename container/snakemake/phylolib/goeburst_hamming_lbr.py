rule Hamming:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        java -jar /app.jar distance hamming --dataset=ml:phylolib/data/datasets/10.txt --out=symmetric:out.txt        
        """

rule GoeBURST:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        java -jar /app.jar /app.jar algorithm goeburst --out=newick:tree.txt --matrix=symmetric:matrix.txt
        """

rule Lbr:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        java -jar /app.jar optimization lbr --tree=newick:tree.txt --dataset=ml:phylolib/data/datasets/10.txt --matrix=symmetric:matrix.txt --out=newick:out.txt
        """