class Solution:
    def shortestPathBinaryMatrix(self, grid):

        if not grid or not grid[0] or grid[0][0] == 1: return -1

        queue = collection.deque()

        queue.append([0, 0])

        dx = (-1, -1, 0, 1, 1, 1, 0, -1)
        dy = (0, -1, -1, -1, 0, 1, 1, 1)

        count = 0

        while queue:

            count += 1
            for i in range(len(queue)):
                curr_pos = queue.popleft()
                x = curr_pos[1]
                y = curr_pos[0]

                for i, j in zip(dx, dy):
                    new_x = j + x
                    new_y = i + y

                    if new_x == len(grid[0]) and new_y == len(grid): return count

                    if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid) and grid[new_y][new_x] == 0:
                        grid[new_y][new_x] = '.'
                        queue.append([new_y, new_x])
        
        return -1


# bfs o(n)
# o(n)

