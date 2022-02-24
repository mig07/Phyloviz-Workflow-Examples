rule Hamming:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        java -jar /app.jar distance hamming --dataset=ml:phylolib/data/datasets/10.txt --out=symmetric:out.txt        
        """

rule Upgma:
    shell:
        """
        docker run -v $HOME/.phylolibVol:/phylolib --workdir /phylolib luanab/phylolib:latest \
        java -jar /app.jar algorithm upgma --out=newick:tree.txt --matrix=symmetric:out.txt        
        """