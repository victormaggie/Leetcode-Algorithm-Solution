class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix and not matrix[0]: return
        if len(matrix) == 1: return matrix[0]
        First_row, First_column, Last_row, Last_column = 0, 0, len(matrix)-1, len(matrix[0])-1
        stack = []
        i, j = 0, 0
        while  First_row < Last_row and  First_column < Last_column:
            
            while j < Last_column:
                stack.append(matrix[i][j])
                j += 1
                
            Last_column -= 1
            
            while i < Last_row:
                stack.append(matrix[i][j])
                i += 1
            
            Last_row -= 1
            
            while j > First_column:

                stack.append(matrix[i][j])
                j -= 1
                
            First_column -= 1
            
            while i > First_row:
                stack.append(matrix[i][j])
                i -= 1
            First_row += 1
            
        if len(matrix) == len(matrix[0]):
            stack.append(matrix[i+1][j+1])
        return stack