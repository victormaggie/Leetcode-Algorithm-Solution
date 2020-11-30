var sortedSquares = function(A) {
    
    let left = 0, right = A.length - 1;
    let maxLen = right;
    let stack = Array(maxLen).fill(0);

    while (left <= right) {
        squareLeft = A[left] * A[left];
        squareRight = A[right] * A[right];
        if (squareLeft > squareRight) {
            stack[maxLen] = squareLeft;
            left ++;
        } else {
            stack[maxLen] = squareRight;
            right --;
        }
        maxLen --;
    }
    return stack;
};

// o(n)
