class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = float('inf')
        for i in range(m):
            for j in range(n):
                # this algorithm can not get the minimum time
                # we need to look the total rotten orange
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

# how to solve this problem when they rotten together !! ---- > first traversal all the rotten orange, and use bfs for all the rotten orange!

## TAKE AWAY:
# 1. use BFS traversal all the rotten orange
# 2. use the queue to do memoization
# 3. when put into the queue, we need to change the value to 2, otherwise the next neighbor will put the node into the queue and calculate again!


# the correct answer!
class Solution:
    def orangesRotting(self, grid):
        # first of all the orange
        queue = collections.deque()
        m, n = len(grid), len(grid[0])
        # use the fresh orange to check the total number of rotten
        freshorg = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    freshorg += 1
        
        # edge case calculation
        if not queue: return -1
        if freshorg == 0: return 0

        time = -1
        direction = [(0,-1), (-1,0), (0,1), (-1, 0)]
        while queue:
            max_len = len(queue)
            for _ in range(k):
                a, b = queue.popleft()
                for k in range(4):
                    x = a + direction[k][0]
                    y = b + direction[k][1]
                    if x >= 0 and x < m and y >=0 and y < n and grid[x][y] == 1:
                        queue.append((x, y))
                        grid[x][y] = 2
                        freshorg -= 1
            time += 1
        
        return time if freshorg == 0 else -1

# time complexity o(N)
# space complexity o(N)
