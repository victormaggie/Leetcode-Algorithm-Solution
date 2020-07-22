class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # DAG graph solution
        
        # A. initialize the graph and indegree
        
        graph = {i: [] for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        
        # B. build the graph and indegree
        
        # ( be aware of the requisite is v !!!)
        # and the indegree one is u
        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        # C. find the source of the graph
        queue = collections.deque()
        for i in indegree:
            if indegree[i] == 0:
                queue.append(i)
        
        res = []
        
        # iterate the queue for the calculation
        while queue:
            max_len = len(queue)
            for _ in range(max_len):
                node = queue.popleft()
                res.append(node)
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
        
        # here is very important!
        # check if it is the DAG
        if len(res) == numCourses:
            return res
        
        return []

# time complexity o(v+e)