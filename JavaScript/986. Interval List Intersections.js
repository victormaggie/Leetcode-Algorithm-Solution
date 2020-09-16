var intervalIntersection = function(A, B) {
    let i = 0, j = 0;
    let ans = [];

    while (i < A.length && j < B.length) {
        low = Math.max(A[i][0], B[j][0]);
        hig = Math.min(A[i][1], B[j][1]);

        if (low <= hig) {
            ans.push([low, hig]);
        }

        A[i][1] > B[j][1] ? j++ : i++; 
    }
    return ans;
}
// o(n) time cplex
// o(n) space cplx
