# TensorFlow Docker File
Tutorial: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/docker/Dockerfile

# How to build docker image
1. in `docker_TensorFlow` folder 
<pre>
$ sudo docker build -t eis/hdd_ml_dev .
</pre>

# How to run docker image
1. start container. name is `hdd_ml_dev`
<pre>
$ sudo docker run -it --name hdd_ml_dev -p 3000:3000 eis/hdd_ml_dev
or 
$ sudo docker run -it --name hdd_ml_dev -v $PWD:/home/adv:rw -p 3000:3000 eis/hdd_ml_dev

</pre>

2. restart container. name is `hdd_ml_dev`
<pre>
$ sudo docker start -ai hdd_ml_dev
</pre>

3. stop container. name is `hdd_ml_dev`
<pre>
$ sudo docker rm  hdd_ml_dev
</pre>
