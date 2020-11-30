var generateMatrix = function(n) {
    
    let left = 0, right = n-1, upper = 0, down = n-1;
    
    let res = Array(n).fill().map(() => Array(n).fill(0));

    let num = 1;
    while (left <= right && upper <= down) {
        
        for (let i = left; i <= right; i++) res[upper][i] = num++;
        upper ++;
        
        for (let i = upper; i <= down; i++) res[i][right] = num++;
        right --;
        
        for (let i = right; i >= left; i--) res[down][i] = num++;
        down --;

        for (let i = down; i >= upper; i--) res[i][left] = num++;
        left ++;
        
    }
    return res;
    
};

// the solution n * n matrix, we do not need to calculate the direction of the matrix
