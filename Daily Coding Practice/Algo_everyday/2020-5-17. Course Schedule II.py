class Solution:
    def findOrder(self, numCourses, prerequisites):
        # DAG -->
        # 1. Initialize the Graph and Inorder
        Graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}

        # 2. Build the graph and indegree
        for items in prerequisites:
            child, parent = items
            Graph[parent].append(child)
            indegree[child] += 1
        
        # 3. Find the source and sink for the calculation
        source = collections.deque()
        for i in indegree:
            if indegree[i] == 0: source.append(i)
        
        # 4. Pop out the source for the calculation
        res = []
        while queue:
            max_len = len(source)
            for _ in range(max_len):
                # o(v) iterate the node
                node = soruce.popleft()
                res.append(node)
                # o(e) iterate the edge
                for child in Graph[node]:
                    indegree[child] += 1
                    if indegree[child == 0:
                        source.append(child)
        if len(res) == len(Graph): return res
        else: return []

# Time complexity o(v + e)
# Space complexity o(v + e)

