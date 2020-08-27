var fourSumCount = function(A, B, C, D) {
    let dict = {};
    
    for (let i = 0; i < A.length; i++){
        for (let j = 0; j < B.length; j++){
            if (!((A[i] + B[j]) in dict)) {
                dict[(A[i] + B[j])] = 0;
            }
            
            dict[(A[i] + B[j])] += 1;
        }
    }
    
    let ans = 0;
    for (let i = 0; i < C.length; i++){
        for (let j = 0; j < D.length; j++){
            if (-(C[i] + D[j]) in dict) {
                ans += dict[-(C[i] + D[j])];
            }
        }
    }
    return ans;
    
};

// hashtable solution 
// 