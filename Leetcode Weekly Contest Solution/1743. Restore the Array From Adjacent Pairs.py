class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        count = collections.defaultdict(int)
        for u, v in a:
            
            graph[u].append(v)
            graph[v].append(u)
            count[u] += 1
            count[v] += 1
        
        start = 0
        for key in count:
            
            if count[key] == 1:
                start = key
                break
        
        visited = set()
        
        ans = []
        def dfs(graph, parent, temp):
            
            nonlocal ans
            
            if len(temp) == len(graph):
                ans = temp[:]
                return
            
            visited.add(parent)
            
            for child in graph[parent]:
                if child not in visited:
                    temp.append(child)
                    visited.add(child)
                    dfs(graph, child, temp)
                    temp.pop()
                    visited.remove(child)
        
        dfs(graph, start, [start])
        return ans
    
