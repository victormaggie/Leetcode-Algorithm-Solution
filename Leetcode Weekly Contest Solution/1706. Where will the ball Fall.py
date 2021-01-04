class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        res = []
        # use the simulation method to find the path
        for i in range(n):
            x, y, z = 0, i, 0
            while x < m:
                
                # on the top of the grid
                if not z:
                    if grid[x][y] == 1:
                        if y + 1 >= n or grid[x][y+1] == -1: y = -1
                        else: 
                            y += 1
                            z = 1
                    
                    else:
                        if y - 1 < 0 or grid[x][y-1] == 1: y = -1
                        else:
                            y -= 1
                            z = 1
                
                else:
                    x += 1
                    z = 0
                
                if y == -1: break
                
            res.append(y)
        
        return res
        
# The simulation question: o(n * m) time complexity 
# 