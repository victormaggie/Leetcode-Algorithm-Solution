
// Clone Graph
// Clone Binary Tree With Random Pointer
// Clone N-ary Tree


var copyRandomList = function(head) {
    const map = new Map();
    function copy(node) {
        if (node == null) return null;
        if (map.get(node) != null) return map.get(node);

        const n = new Node(node.val);
        map.set(node, n);

        n.next = copy(node.next);
        n.random = copy(node.random);
        return n;
    }
    return copy(head);
}