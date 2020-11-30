var cloneGraph = function(node) {
    
    visited = {};
    return recursion(node);
    function recursion(node){
        
        if (!node) return null;
        if (visited[node.val]) return visited[node.val];
        
        // clone node and clone edge
        const root = new Node(node.val);
        visited[root.val] = root;
        if (!node.neighbors) return root;
        for (let i = 0; i < node.neighbors.length; i++) {
            root.neighbors.push(recursion(node.neighbors[i]));
        }
        return root;
    }
};

//colone graph