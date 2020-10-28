var rotate = function(matrix) {
    let n = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }

    for (let i = 0; i < n; i++){
        matrix[i].reverse();
    }
}

// o(n*m)

var rotat = function(matrix) {
    let n = matrix.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < i; j++) {
            [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]];
        }
    }
    for (let i = 0; i < n; i++)
        for (let j = 0, k = n - 1; j < k; j++, k--)
            [matrix[i][j], matrix[i][k]] = [matrix[i][k], matrix[i][j]];
}

