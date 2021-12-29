res_dir=../../res/phylolib
java -jar $res_dir/PhyloLib-1.0-SNAPSHOT.jar algorithm upgma --out=newick:tree.txt : distance hamming --dataset=ml:$base_dir/datasets/10.txt
