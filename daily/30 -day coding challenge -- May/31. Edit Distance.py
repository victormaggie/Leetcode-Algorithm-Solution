class solution:
    # Levenshtein distance
    def minDistance(self, word1, word2):
        m = len(word2)
        n = len(word1)

        if m * n == 0: return m + n

        # define dp
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(1, n+1):
            dp[0][i] = i
        
        for j in range(1, m+1):
            dp[j][0] = j

        # transition matrix for the calculation
        for i in rnge(1, m+1):
            for j in range(1, n+1):
                if word2[i-1] != word1[j-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        return dp[m][n]

# time complexity o(m*n)
# space complexity o(m*n)
