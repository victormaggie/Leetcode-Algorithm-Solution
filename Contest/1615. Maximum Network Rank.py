class Solution:
    def maximalNetWorkRank(self, n, roads):
        graph = {i : set() for i in range(n)}

        for i, (a, b) in enumerate(roads):
            graph[a].add(i)
            graph[b].add(i)
        
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                num = len(graph[i]) + len(graph[j])
                for v in graph[i]:
                    if v in graph[j]:
                        num -= 1
                
                if ans < num:
                    ans = num
        return ans

# o(n^2)
