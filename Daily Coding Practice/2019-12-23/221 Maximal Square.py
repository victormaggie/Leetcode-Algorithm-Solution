class Solution:
    def maximalSquare(self, matrix):
        if not matrix: return 0
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        
        res = max(max(row) for row in dp)
        
        return res ** 2