# Variables
res_dir=../../../res/phylolib/data
container_file_dir=$HOME/.phylolibLogs/files:/files
container_log_dir=$HOME/.phylolibLogs/logs:/logs

# Turn docker service on
sudo systemctl start docker.service containerd.service
# Create container with 1 volume to supply data (files volume)
docker container create --name phylolib -v $container_file_dir luanab/phylolib:latest
# Copy dataset and matrices to files volume
docker cp $res_dir/. phylolib:/files
# Run the container
docker run -v $container_file_dir -v $container_log_dir phylolib algorithm upgma --out=newick:logs/tree.txt : distance hamming --dataset=ml:files/datasets/10.txt
