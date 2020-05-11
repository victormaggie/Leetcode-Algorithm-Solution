class Solution:
    def findJudge(self, N, trust):
        # solve this problem as Graph
        # Indegree = 0
        # Outdegree = N-1
        indegree = {i: [] for i in range(1, N+1)}
        Outdegree = {i: [] for i in range(1, N+1)}
        for i, j in trust:
            indegree[i].append(j)
            outdegree[j].append(i)
        for i in indegree:
            if indegree[i] == [] and len(outdegree) == N-1:
                return i
        return -1

# time complexity o(v+e)
# space complexity o(v+e)