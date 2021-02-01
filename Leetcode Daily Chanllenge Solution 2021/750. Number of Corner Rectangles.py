
# This question cannot use this Dynamic programming
# Cuz the 

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m , n = len(grid), len(grid[0])
        
        dp = [[False] * n for i in range(m)]
        
        for i in range(n):
            
            dp[0][i] = grid[0][i] == 1
        
        for i in range(m):
            
            dp[i][0] = grid[i][0] == 1
        
        ans = 0
        
        for i in range(1, m):
            for j in range(1, n):
                
                if grid[i][j] == 1:
                    if dp[i-1][j] and dp[i-1][j-1] and dp[i][j-1]:
                        ans += 1
                
                if dp[i-1][j] or dp[i][j-1]:
                    dp[i][j] = True
                    
        return ans
        
        
    def countCornerRectangles(self, grid):
        
        count = collections.Counter()
        
        ans = 0
        
        for row in grid:
            
            for c1, v1 in enumerate(row):
                
                if v1:
                    for c2 in range(c1+1, len(row)):
                        
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        
        return ans
        