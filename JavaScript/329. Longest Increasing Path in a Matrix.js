/**
 * @param {number[][]} matrix
 * @return {number}
 */
var longestIncreasingPath = function(matrix) {
    
    if (matrix == null || matrix[0] == null) return 0;
    
    let row = matrix.length;
    let col = matrix[0].length;
    let ans = 0;
    const dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]];
    
    // define the Memorization here
    let memo = [...Array(row)].map(() => Array(col).fill(null))
    
    
    const recur = (x, y) => {
        if (memo[x][y] != null) return memo[x][y];
        
        let max = 1;
        for (const [dx, dy] of dirs) {
            const j = y + dy;
            const i = x + dx;
            
            if (i >= 0 && j >= 0 && i < row && j < col && matrix[i][j] > matrix[x][y]) {
                const len = recur(i, j) + 1;
                max = Math.max(max, len);
            }
        }
        memo[x][y] = max;
        return max;
    }
    
    for (let i=0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            
            ans = Math.max(ans, recur(i, j));
        }
    }
    
    return ans;
    
};

// time complexity (o(mn))
// space complexity o(mn)

