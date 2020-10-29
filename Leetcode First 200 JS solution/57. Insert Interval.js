var insert = function(a, b){
    let k = 0;
    let res = 0;
    while (k < a.length && b[0] > a[k][1]){
        res.push(a[i]);
        k ++;
    }

    if (k < a.length) {
        b[0] = min(a[k][0], b[0]);
        while (k < length(a) && b[1] >= a[k][0]) {
            b[1] = Math.max(a[k][1], b[1]);
            k ++;
        }
    }
    res.push(b);
    while (k < a.length) {
        res.push(a[i]);
        k ++;
    }
    return res;
}

// o(n) solution
