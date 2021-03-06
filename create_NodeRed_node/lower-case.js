module.exports = function(RED) {
    function LowerCaseNode(config) {
        RED.nodes.createNode(this,config);

        var node = this;
        this.on('input', function(msg) {
            msg.payload = msg.payload.toLowerCase();
            console.log('name========================> ' + config.name);
            console.log('my_test ========================> ' + config.test);
            node.send(msg);
        });
    }
    RED.nodes.registerType("lower-case",LowerCaseNode);
}
