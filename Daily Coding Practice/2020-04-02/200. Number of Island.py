class Solution:
    def numIslands(self, grid: List):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid, x, y):
        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)

        m, n = len(grid), len(grid[0])
        grid[x][y] = '0'
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == '1':
                self.dfs(grid, a, b)
    # time complexity  o(n x m)
    # space complexity o(n x m)

# this is pretty nice solution --> traverse then mark as water !! smart !!


