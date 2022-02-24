res_dir=../../../res/phylolib
java -jar $res_dir/jar/PhyloLib-1.0-SNAPSHOT.jar algorithm goeburst --out=newick:tree.txt -m=symmetric:$res_dir/data/matrices/10.txt : distance hamming --dataset=ml:$res_dir/data/datasets/10.txt : optimization lbr --out=newick:out.txt
