var inorderSuccessor = function(root, p) {
    let head = 0;
    let flag = true;
    let currValue = Number.MAX_VALUE;

    // inorder traversal here and the order
    function dfs(root) {
        if (!root) return ;
        // left
        if (root.left) dfs(root.left);

        if (root == p) {
            flag == true;
            currValue = root.val;
        }

        if (root.val > currValue && flag == true) {
            head = root;
            flag = false;
            return 
        }

        if (root.right) dfs(root.right)
    }

    if (head) return head;
    return null;
}

// traversal o(n)

