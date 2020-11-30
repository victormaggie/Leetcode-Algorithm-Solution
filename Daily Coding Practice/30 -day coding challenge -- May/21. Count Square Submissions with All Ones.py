class Solution:
    def countSquares(self, matrix):
        dp = [[0 for j in range(len(matrix[0]) + 1)] for i in range(len(matrix) + 1)]
        count = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0]) + 1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        
        count = sum([sum(i) for i in dp])
        return count

# time complexity o(m+n)
# space complexity o(m+n)

