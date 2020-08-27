var isMonotonic = function(A){
    let flag = null;

    for (let i = 0; i < A.length-1; i++){
        if (A[i] === A[i+1]){
            continue;
        } else {
            if (flag === null){
                flag = (A[i] > A[i+1]);
            }
            if (flag !== (A[i] > A[i+1])){
                return false;
            }
        }
    }
    return true;
};

// time complexity o(n)
// space complexity o(1)


// one pass solution

var isMonotonic = function(A){
    let increasing = true;
    let decreasing = true;

    for (let i = 0; i < A.length-1; i++){
        if (A[i] > A[i+1]) increasing = false;
        if (A[i] < A[i+1]) decreasing = false;
    }
    return increasing || decreasing;
}

// time complexity o(n)
// space complexity o(1)