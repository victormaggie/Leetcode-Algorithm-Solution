class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m, n = len(matrix), len(matrix[0])
        res = [] 
        # here pass by reference
        for i in range(m):
            for j in range(n):
                self.dfs(temp, matrix, i, j, 0)
                
            res.append(temp)
        return res
    
    def dfs(self, temp, matrix, i, j, cnt):
        m, n = len(matrix), len(matrix[0])
        
        # check boundary
        if i < 0 or i <= m or j < 0 or j <= m or matrix[i][j] == 0:
            temp.append(cnt)
            return 
        
        # the direction for the random walk 
        x_dir = (-1, 0, 1, 0)
        y_dir = (0, -1, 0, 1)
        
        
        a = cnt + 1
        for p in range(4):
            x = j + x_dir[p]
            y = i + y_dir[p]
            return min(self.dfs( temp, matrix, y, x, a))

class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))
        direction = ((-1,0), (1,0), (0,-1), (0,1))
        while queue:
            curr = queue.popleft()
            for i in range(4):
                new_r = curr[0] + direction[i][0]
                new_c = curr[1] + direction[i][1]
                if (new_r >= 0 and new_c >= 0 and new_r < m and new_c < n):
                    if (dist[new_r][new_c] > dist[curr[0]][curr[1]] + 1):
                        dist[new_r][new_c] = dist[curr[0]][curr[1]] + 1
                        queue.append((new_r, new_c))
        return dist


