var lengthOfLastWord = function(s) {
    
    if (s.length == 0 || s.trim().length == 0) return 0;
    s = s.trim();
    let ans = 0; k = s.length - 1;
    
    while (s[k] !== ' ' && k >= 0){
        ans ++;
        k --;
    }
    return ans;
};

// o(n)
