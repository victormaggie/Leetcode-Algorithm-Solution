class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not grid or not grid[0]: return 
        
        m, n = len(grid), len(grid[0])
        
        def dfs(grid, i, j):
            
            # stop condition here
            if grid[i][j] == 'X': return
            
            grid[i][j] = '.'
            
            dx = (-1, 0, 1, 0)
            dy = (0, -1, 0, 1)
            
            for k in range(4):
                
                new_x = j + dx[k]
                new_y = i + dy[k]
                
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_y][new_x] == 'O':
                    
                    dfs(grid, new_y, new_x)
        
        # iterate the upper and lower bound
        
        for j in range(n):

            if grid[0][j] == 'O': dfs(grid, 0, j)
            if grid[m-1][j] == 'O': dfs(grid, m-1, j)
        
        
        for i in range(m):
            
            if grid[i][0] == 'O': dfs(grid, i, 0)
            if grid[i][n-1] == 'O': dfs(grid, i, n-1)
            
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == 'O': grid[i][j] = 'X'
                
                if grid[i][j] == '.': grid[i][j] = 'O'
        
        return grid