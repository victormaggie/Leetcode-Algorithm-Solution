class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]: return 0
        dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        num_len = max(max(i) for i in dp)
        return num_len ** 2

# time complexity o(N*M)
# space complexity o(N*M)


# There has better dynamic solution 
# Look ---->


