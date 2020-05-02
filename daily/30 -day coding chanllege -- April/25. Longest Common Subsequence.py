class Solution:
    def longestCommonSubsequence(self, text1, text2):
        # dynamic programming
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # initialization
        for i in range(m+1):
            dp[0][i] = 0
        
        for j in range(n+1):
            dp[j][0] = 0
        
        # transition matrix for the dynamic matrics
        for i in range(n):
            for j in range(m):
                if text2[i] == text1[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                
        return dp[-1][-1]

# time complexity (o(N*M))
# space complexity(o(M + N))

##################### Need optimization for this questions ######################

