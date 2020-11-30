var countAndSay = function(n) {
    const f = Array.from({length: n});
    f[0] = '1';
    for(let i = 1; i < n; i ++) {
        let j = 0, str = f[i - 1], res = "";
        const sl = str.length;
        while(j < sl) {
            let c = str[j], k = 1;
            while(j + 1 < sl && str[j + 1] == str[j]) j ++, k ++;
            res += k + "" + c;
            j ++;
        }
        f[i] = res;
    }
    return f[n - 1];
};

//