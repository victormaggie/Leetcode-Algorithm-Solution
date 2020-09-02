class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # backtracking solution 
        if not matrix or not matrix[0]: return 0
        
        m, n = len(matrix), len(matrix[0])
        
        ans = 0
        for i in range(m):
            for j in range(n):
                
                a = self.rec(matrix, m, n, i, j, 1)
                print(a)
                ans = max(ans, a)
        
        return ans
    
    
    def rec(self, matrix, m, n, i, j, path):
        
        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)
        
        for k in range(4):
            new_x = j + dx[k]
            new_y = i + dy[k]
            
            if 0 <= new_y < m and 0 <= new_x < n and matrix[new_y][new_x] > matrix[i][j]:
                new_path = path + 1
                self.rec(matrix, m, n, new_y, new_x, new_path)
                
        return path