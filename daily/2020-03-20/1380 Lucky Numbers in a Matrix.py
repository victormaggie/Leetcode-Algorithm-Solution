class Solution:
    def luckyNumbers(self, matrix):
        if not matrix or not matrix[0]:
            return False
        
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

    
    def luckyNumbers1(self, matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])

        for i in range(row_len):
            # find the column --> smallest
            min_index = matrix[i].index(min(matrix[i]))
            Flag = True
            for j in range(row_len):
                if matrix[i][min_index] < matrix[j][min_index]:
                    Flag = False
            if Flag:
                return [matrix[i]][min_index]
        return []
                