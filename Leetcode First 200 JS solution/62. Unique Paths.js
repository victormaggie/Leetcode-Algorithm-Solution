var uniquePaths = function(m, n) {
    if (!m || !n) return 0;
    let matrix = Array(m).fill().map(() => Array(n).fill(0));
    matrix[0][0] = 1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (i) matrix[i][j] += matrix[i-1][j];
            if (j) matrix[i][j] += matrix[i][j-1];
        }
    }
    return matrix[m-1][n-1];
}

// o(n * m)

