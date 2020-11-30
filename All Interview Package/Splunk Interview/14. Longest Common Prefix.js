var longestCommonPrefix = function(strs) {
    
    ans = '';
    if (!strs || !strs[0]) return ''
    // iterate the first word and check the answer!
    for (let i = 0; i < strs[0].length; i++) {
        char = strs[0][i];
        for (let j = 1; j < strs.length; j++) {
            if (i > strs[j].length || char !== strs[j][i]) return ans;
        }
        ans += char;
    }
    return ans;
};

// o(n * m) complexity
