class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not matrix or not matrix[0]: return []
        
        pacific = set()
        atlantic = set()
        
        m , n = len(matrix), len(matrix[0])
        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)
        
        def dfs(visited, x, y):
            
            visited.add((x, y))
            
            for k in range(4):
                new_x = y + dx[k]
                new_y = x + dy[k]
                
                if 0 <= new_y < m and 0 <= new_x < n and ((new_y, new_x) not in visited) and matrix[new_y][new_x] >= matrix[x][y]:
                    dfs(visited, new_y, new_x)
        
        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n-1)
        
        for j in range(n):
            dfs(pacific, 0, j)
            dfs(atlantic, m-1, j)
        
        return list(pacific.intersection(atlantic))