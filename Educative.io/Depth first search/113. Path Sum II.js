var pathSum = function(root, sum) {
    
    if (!root) return [];
    
    function dfs(root, sum, path) {
        
        sum -= root.val;
        path.push(root.val);
        if (root.left === null && root.right === null) {
            
            if (sum === 0) res.push(path);
            return;
        }
        if (root.left) dfs(root.left, sum, [...path]);
        if (root.right) dfs(root.right, sum, [...path]);
    }
    
    res = [];
    dfs(root, sum, []);
    return res;
};

// o(N);
