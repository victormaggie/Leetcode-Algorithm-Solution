var merge = function(itv) {
    
    itv.sort((a, b) => a[0] - b[0]);
    
    if (itv.length < 1) return itv;
    
    let ans = [];
    ans.push(itv[0])
    
    for (let i = 1; i < itv.length; i++) {
        
        if (ans[ans.length-1][1] < itv[i][0]){
            ans.push(itv[i]);
        } else {
            let value = ans.pop();
            const front = Math.min(value[0], itv[i][0]);
            const end   = Math.max(value[1], itv[i][1]);
            ans.push([front, end]);
        }
    }
    return ans;
};

// o(n) solution
// 