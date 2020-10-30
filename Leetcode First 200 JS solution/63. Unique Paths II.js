var uniquePathsWithObstacles = function(obstacleGrid) {
    
    
    if (obstacleGrid[0][0] == 1) return 0;
    let m = obstacleGrid.length, n = obstacleGrid[0].length;
    if (m == 0 || n == 0) return 0;
    
    let matrix = Array(m).fill(0).map(() => Array(n).fill(0))
    
    matrix[0][0] = 1;
    
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {

            if (!obstacleGrid[i][j]) {
                if (i) matrix[i][j] += matrix[i-1][j];
                if (j) matrix[i][j] += matrix[i][j-1];
                }
            }
        }

return matrix[m-1][n-1]
};


