var minCut = function(s) {
    dp = Array(s.length).fill(false)
        .map(() => Array(s.length)
        .fill(false));

    for (let i=0; i < s.length; i++) {
        for (let j=0; j <= i; j++) {
            if (i ==j) dp[i][j] = true;
            else if (s.charAt(i) == s.charAt(j)) {
                if ( i - 1 < j + 1 || dp[j+1][i-1]) {
                    dp[j][i] = true;
                }
            }
        }
    }

    let ans = Array(s.length).fill(1e8);
    for (let i=0; i < s.length; i++) {
        for (let j=0; j <= i; j++) {
            if(dp[j][i]) {
                ans[i] = j - 1 < 0 ? 0 : Math.min(ans[i], ans[j-1] + 1)
            }
        }
    }
    return ans[s.length-1];
};

// time complexity o(n^2)
// space o(n^2)

