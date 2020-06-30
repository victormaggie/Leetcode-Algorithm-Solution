class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP graph define
        graph = [[0 for i in range(m)] for j in range(n)]
        dp = [[-1 for i in range(m)] for j in range(n)]

        def dfs(i, j):
            if (i, j) == (0, 0): return 1
            if i < 0 and j < 0: return 0
            if dp[i][j] != -1: return dp[i][j]

            dp[i][j] = dfs(i-1, j) + dfs(i, j-1)
            return dp[i][j]
        
        return dfs(n-1, m-1)

# dynamic programming o(n*m)
# space complexity o(n*m)

    def uniquePaths_bottom_up(self, m: int, n: int) -> int:
        dp = [[1 for i in range(m)] for j in range(n)]
        
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

# dynamic programming o(n*m)
# space complexity o(n*m)

