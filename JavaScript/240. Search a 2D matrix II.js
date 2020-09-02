var searchMatrix = function(matrix, target) {
    
    // binary search solution; 
    if (!matrix || !matrix[0]) return false;

    const RowLen = matrix.length - 1;
    const ColLen = matrix[0].length - 1;

    curr_row = 0;
    curr_col = ColLen;

    while (curr_col >= 0 && curr_row >= ColLen) {
        if (matrix[curr_row][curr_col] == target) {
            return true;
        } else if (matrix[curr_row][curr_col] > target){
            curr_col--;
        } else{
            curr_row++;
        }
    }
    return false;
}

// o(n+m) time complexity
// o(1) space complexity
