class Solution:
    def combine(self, n, k):
        res = []
        path = []
        index = 1
        self.dfs(n, res, path, index, k)
        return res
    
    def dfs(self, n, res, path, index, k):
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(index, n+1):
            path.append(i)
            self.dfs(n, res, path, i+1, k)
            path.pop()