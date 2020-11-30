class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor:int) -> List[List[int]]:
        if not image or not image[0]: return []
        if not newColor: return image
        self.starting = image[sr][sc]
        m, n = len(image), len(image[0])

        for i in range(m):
            for j in range(n):
                if (i, j) == (sr, sc):
                    self.dfs(image, m, n, sr, sc, newColor)
        return image
    
    def dfs(self, image, m, n, sr, sc, newColor):
        if image[sr][sc] == newColor: return 

        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0 ,1)
        image[sr][sc] = newColor
        for k in range(4):
            new_x = dx[k] + sc
            new_y = dy[k] + sr
            if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m and image[new_y][new_x] == self.starting:
                self.dfs(image, m, n, new_y, new_x, newColor)
        
# time complexity: o(N)
# space complexity: o(N)

    def floodFill_BFS(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]: return []
        if not newColor: return image
        starting = image[sr][sc]
        m, n = len(image), len(image[0])
        queue = collections.deque()
        queue.append((sr, sc))

        dx = (-1, 0, 1, 0)
        dy = (0, -1, 0, 1)
        while queue:
            max_len = len(queue)
            for _ in range(max_len):
                y, x = queue.popleft()
                for i in range(4):
                    new_x = dx[i] + x
                    new_y = dy[i] + y
                    if new_x >= 0 and new_y >= 0 and new_x < n and new_y < m:
                        if image[new_y][new_x] == starting:
                            queue.append((new_y, new_x))
                            image[new_y][new_x] = newColor
    
        return image


        
