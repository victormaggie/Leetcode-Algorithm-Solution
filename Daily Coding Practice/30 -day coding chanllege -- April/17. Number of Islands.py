class solution:
    def numIslands(self, grid):
        # edge case
        if not grid or not grid[0]: return 0
        # edge case 1 
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0":
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid,  x, y):
        # the moving direction
        # here the direction transformation 
        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)
        m, n = len(grid), len(grid[0])
        # here relabel the data here !
        grid[x][y] = "0"
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            '''
            x = x + dx[i]
            y = y + dy[i]
            this is bug --> cannot update x!
            '''

            if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == '1':
                self.dfs(grid, a, b)

# use the dfs stop condition to solve this problem

class solution:
    def numIslands(self, grid):
        # edge case 
        if not grid or not grid[0]: return 0
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '0':
                    res += 1
                    self.dfs(grid, m, n, i, j)
        return res

    def dfs(self, grid, m, n, i, j):
        # stop condition
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        # four direction of the matrix
        dy = (-1, 0, 1, 0)
        dx = (0, -1, 0, 1)
        for k in range(4):
            a = i + dx[k]
            b = j + dy[k]
            self.dfs(grid,  m, n, a, b)








