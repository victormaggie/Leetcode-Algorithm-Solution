var convert = function(s, numRows) {
    
    if (numRows == 1 || s.length == 1) return s;

    let stack = [];
    for (let i = 0; i < numRows; i++) stack.push('');
    let step = 1, row = 0;
    for (let char of s){
        stack[row] += char;
        if (row == 0) {
            step = 1;
        } else if (row == numRows - 1) {
            step = -1
        }
    }
    return stack.join('');
}

// o(n) time
// o(n) space