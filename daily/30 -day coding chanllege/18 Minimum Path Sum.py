class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        
        for j in range(1, m):
            dp[j][0] = grid[j][0] + dp[j-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]

# return the last one value
# time complexity o(n)
# space complexity o(m+n)

# be aware that if we use dp = [[0]*n]*m ---> every element is a copy of the last row, so it will change!!
# we need to use for to generate matrix !!!