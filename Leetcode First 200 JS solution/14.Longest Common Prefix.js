var longestCommonPrefix = function(strs) {

    if (strs.length === 0 || strs[0].length === 0) return "";

    let ans = '';
    let count = 0;
    while (true) {
        const char = strs[0][count];

        for (let i = 0; i < strs.length; i++) {
            if (count === strs[i].length || strs[i][count] != char) {
                return ans;
            }
        }
        ans += char;
        count ++;
    }
    return ans;
}

// o( total length of the charcter)