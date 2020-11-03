var generateParenthesis = function(n) {
    // brute force solution;
    let res = new Set();
    dfs(n, n, '');
    return [...res];

    function dfs(leftNumber, rightNumber, path){
        if (leftNumber > rightNumber) return;
        if (leftNumber === 0){
            path += ')'.repeat(rightNumber);
            res.add(path);
            return;
        }
        dfs(leftNumber-1, rightNumber, path+'(');
        dfs(leftNumber, rightNumber-1, path+')');
    }
};

// this method is not that good, we need to consider the duplicate 


var generateParenthesis = function(n) {
    
    let res = [];
    dfs(0, 0, '');
    return res;

    function dfs(leftNumber, rightNumber, path) {
        if (leftNumber == n && rightNumber == n) {
            res.push(path);
            return;
        }
        // keep the valid parenthese, leftNumber > right !!! 
        if (leftNumber > rightNumber && rightNumber < n) dfs(leftNumber, rightNumber +1 , path + ')')
        // we can add new value anytime, if its number is less than n
        if (leftNumber < n) dfs(leftNumber+1, rightNumber, path+'(')
    }
}

var generateParenthesis = function(n) {
    
    // first 1: left has
    // second 2: right > -->
    
    let res = [];
    let left = n, right = n
    recursion(left, right, '');
    return res;
    
    function recursion(left, right, temp){
        if (left ==0 && right == 0){
            res.push(temp);
            return;
        }
        
        if (left || left >= right) recursion(left-1, right, temp + '(');
        if (right > left) recursion(left, right-1, temp+')')
    }
};

