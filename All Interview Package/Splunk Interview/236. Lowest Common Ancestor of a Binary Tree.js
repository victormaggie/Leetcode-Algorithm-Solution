var lowestCommonAncestor = function(root, p, q) {
    function recursion(node) {
        if (!node) return;
        if (node == p || node == q) return node;

        const left = recursion(node.left);
        const right = recursion(node.right);

        if (left && right) return node;
        return left || right;
    }
    return recursion(root);
}
// o(n)


