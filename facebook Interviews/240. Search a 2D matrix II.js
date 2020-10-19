var searchMatrix = function (matrix, target) {
    if (matrix.length == 0 || matrix[0].length == 0) return false;

    const m = matrix.length;
    const n = matrix[0].length;

    let col = n - 1;
    let row = 0;

    while (col >= 0 && row < m) {
        curr = matrix[row][col];
        if (curr > target) {
            col --;
        } else if (curr < target) {
            row ++;
        } else {
            return true;
        }
    }
    return false;
};

// time complexity o(n *m)