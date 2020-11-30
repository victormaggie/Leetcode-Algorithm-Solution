class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
    
        zigzag = ['' for x in range(numRows)]
        row, step = 0, 1
        for char in s:
            zigzag[row] += char
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(zigzag)


