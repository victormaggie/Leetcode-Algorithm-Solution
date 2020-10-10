def sortMatrix(matrix, k):

    row, col = len(matrix), len(matrix[0])

    new = [[0 for i in range(row)] for j in range(row)]
    k = k % 4
    for i in range(row):
        for j in range(col):

            if i - j == 0 or i + j == row - 1:
                new[i][j] = matrix[i][j] 
            
            else:
                if k == 1:
                    new[j][i] = matrix[i][j]
                    print(new[(j + col//2)%col][i], '///ssss', j, i)
                elif k == 2:
                    new[i][row-j] = matrix[i][j]
                
                elif k == 3:
                    neww[row-j][i] = matrix[i][j]

    return new


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

k = 1

print(sortMatrix(m, k))


