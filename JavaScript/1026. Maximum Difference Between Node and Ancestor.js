var maxAncestorDiff = function(root){

    const helper = (node, max, min) => {
        if (node === null) {
            return max - min;
        }
        max = Math.max(max, node.val);
        min = Math.min(min, node.val);
        return Math.max(helper(node.left, max, min), helper(node.right, max, min))
    }
    return helper(root, root.val, root.val);

};