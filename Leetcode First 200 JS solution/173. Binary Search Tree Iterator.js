var BSTIterator = function (root) {
    stack = [];
    while (root) {
        stack.unshift(root);
        root = root.left;
    }
};

BSTIterator.prototype.next = function() {
    root = stack[0];
    stack.shift();
    value = root.val;
    root = root.right;
    while (root) {
        stack.unshift(root);
        root = root.left;
    }
    return value;
}

BSTIterator.prototype.hasNext = function() {
    return stack.length;
}

// time complexity o(n)
// space complexity o(n)

