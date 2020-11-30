class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]: return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, m, n, i, j)
        return count
    
    
    def dfs(self, grid, m, n, i, j):
        
        if grid[i][j] == '0':
            return 
        
        grid[i][j] = '.'
        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)
        for k in range(4):
            new_x = j + dx[k]
            new_y = i + dy[k]
            
            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and grid[new_y][new_x] == '1':
                self.dfs(grid, m, n, new_y, new_x)