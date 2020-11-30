var diagnalSum = function(mat) {
    let row = mat.length;
    let res = 0;

    for (let i = 0; i < row; i++) {
        res += mat[i][i];
        if (row & 1) {
            if (i !== (row-1)/2) {
                res += mat[row-1-i][i];
            }
        } else {
            res += mat[row-1-i][i];
        }
    }
    return res;
};


// solution 2

var diagnalSum = function(mat) {
    let row = mat.length;
    let res = 0
    for (let i = 0; i < row; i++) {
        res += mat[i][i] + mat[row-1-i][i];
    }

    if (row & 1) {
        return ans - mat[(row-1)/2][(row-1)/2];
    }

    return ans;
}