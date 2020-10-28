var totalNQueens = function(n) {
    
    let col = Array(n).fill(0);
    let diagnal = Array(2 * n ).fill(0);
    let n_diagnal = Array(2 * n).fill(0);
    
    // dfs find all the solution
    
    let ans = dfs (0);
    return ans;
    
    function dfs(idx){
        
        if (n === idx) {

            return 1;
        }
        res = 0;
        for (let j = 0; j < n; j ++) {
            if (col[j] == 0 && diagnal[n+idx-j] == 0 && n_diagnal[idx+j] == 0){
                col[j] = diagnal[n+idx-j] = n_diagnal[idx+j] = 1;
                res += dfs(idx + 1);
                col[j] = diagnal[n+idx-j] = n_diagnal[idx+j] = 0;
            }
        }
        return res;
    }
    
};

// dfs find all the solution here!
