class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    new_grid = copy.deepcopy(grid)
                    new_time = self.bfs(new_grid, i, j)
                    time = min(time, new_time)
                    print(i, j)

        for i in range(m):
            for j in range(n):
                if new_grid[i][j] == 1:
                    return -1
        return time
    
    def bfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]      
        queue = collections.deque()
        count = -1
        queue.append((i,j))
        while queue: 
            count += 1
            max_len = len(queue)
            for i in range(0, max_len):
                new_rotten = queue.popleft()
                grid[new_rotten[0]][new_rotten[1]] = 2
                for k in range(4):
                    a = new_rotten[0] + direction[k][0]
                    b = new_rotten[1] + direction[k][1]
                    if a >= 0 and a < m and b >= 0 and b < n and grid[a][b] == 1:
                        #print(a, b)
                        if (a, b) not in queue:
                            queue.append((a,b))
        return count

# how to solve this problem when they rotten together !!