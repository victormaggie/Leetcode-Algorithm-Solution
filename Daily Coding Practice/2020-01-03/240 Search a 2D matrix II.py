class Solution(object):
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]:
            return False
        
        row, col = len(matrix), len(matrix[0])

        cur_row, cur_col = 0, col-1
        while cur_row < row and cur_col >= 0:
            if matrix[cur_row][cur_col] >= 0:
                return True
            elif matrix[cur_row][cur_col] > target:
                cur_col -= 1
            else:
                cur_row += 1

        return False

# time complexity (o(n+m))
# space complexity o(1)
