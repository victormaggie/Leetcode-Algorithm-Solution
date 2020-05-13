# This is great question! Super solution!
# Time complexity o(v + e)
# Space complexity o(v + e)

class Solution:
    def findMinHeightTrees(self, n, edges):
        # edge case
        if not n: return 0
        if n == 1: return [0]

        # a. Initialize the Graph
        Graph = {i: [] for i in range(n)}
        inDegree = {i: 0 for i in range(n)}

        # b. Build the Graph
        for parent, child in range(edges):
            Graph[parent].append(child)
            Graph[child].append(parent)
            inDegree[child] += 1
            inDegree[parent] += 1

        # c. Find the source and sink
        queue = collections.deque()
        for i in inDegree:
            if inDegree[i] == 1:
                # leave node  ---> this is pretty smart
                queue.append(i)
        total_node = n
        while totoal_node > 2:
            leave_size = len(queue)
            total_node -= leave_size
            for i in range(leave_size):
                vertext = queue.popleft()
                for child in Graph[vertext]:
                    inDegree[child] -= 1
                    if inDegree[child] == 1:
                        queue.append(child)
        return list(queue)
    
# time complexity o(v + e)
# space complexity o(v + e)

