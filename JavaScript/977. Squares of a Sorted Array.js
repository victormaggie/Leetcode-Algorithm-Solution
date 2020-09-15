
var sortedSquares = function(A) {

    let left = 0;
    let right = A.length-1;
    const ans = Array(A.length).fill(0);
    let i = right;
    while (left <= right) {
        const leftPower = A[left]**2;
        const rightPower = A[right]**2;

        if (leftPower > rightPower) {
            ans[i] = leftPower;
            left++;
        } else {
            ans[i] = rightPower;
            rightPower--;
        }
        i--;
    }
    return ans;
};


