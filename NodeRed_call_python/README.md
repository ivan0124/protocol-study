#Node-Red Tutorial
http://nodered.org/docs/creating-nodes/

# Setup `python-shell` for Node.js(Node-Red) calling python
1. install python-shell
<pre>
$ sudo npm install python-shell
</pre>

https://github.com/extrabacon/python-shell

#Code Description
1.set Python script path and argument
<pre>
    var options = {
        scriptPath: '/mnt/my-study/NodeRed_call_python', 
        args: ['value1', 'value2', 'value3']
     };
     var pyshell = new PythonShell('hello.py', options);
</pre>

# How to test (for Ubuntu 14.04)
1. copy node `lower-case.js, lower-case.html, hello.py` to `~/.node-red/nodes`
2. cd ~/.node-red/nodes
3. run `node-red`
4. our Node-Red component in browser

![image link](https://github.com/ivan0124/my-study/blob/master/create_NodeRed_node/image/20160817_node_red.png)
