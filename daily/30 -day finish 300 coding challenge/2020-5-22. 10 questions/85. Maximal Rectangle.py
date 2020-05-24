class Solution:
    def maximumRectangle(self, matrix):
        dp = [[0 for i in range(matrix[0])] for j in range(len(matrix))]
        area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # o(n*m)
                if matrix[i][j] == '0': continue
                width = dp[i][j] = dp[i][j-1] + 1 if j else 1
                # o(n)
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    height = i - k + 1
                    area = max(area, width * height)
        return area

# time complexity o(n^2 * m)
# space complexity o(n*m)
