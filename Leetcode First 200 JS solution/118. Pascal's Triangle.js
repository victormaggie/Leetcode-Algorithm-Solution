var generate = function(numRows) {

    if (numRows == 0) return [];
    if (numRows == 1) return [[1]];

    let Tri = [[1]];
    for (let i = 0; i < numRows; i++) {
        row = [1];
        for (let j = 1; j < i; j++) {
            row.push(Tri[i-1][j-1] + Tri[i-1][j]);
        }
        row.push(1);
        Tri.push(row);
    }
    return Tri;
};

// time complexity o(n)
// space complexity o(n)
