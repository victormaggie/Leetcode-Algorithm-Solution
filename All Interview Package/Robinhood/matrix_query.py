def matrixQueries(n, m, queries):

    r = list(range(1, n+1))
    c = list(range(1, m+1))

    matrix = [[1 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            matrix[i][j] = (i+1) * (j+1)

    ans = []
    for elem in queries:
        if len(elem) == 1:
            ans.append(matrix[r[0]-1][c[0]-1])
        
        else:

            if elem[0] == 1:
                r.remove(elem[1])
            else:
                c.remove(elem[1])
    
    return ans

queries = [[0], [1,2], [0], [2,1],[0],[1,1],[0]]
print(matrixQueries(3, 4, queries))

# simple solution here
