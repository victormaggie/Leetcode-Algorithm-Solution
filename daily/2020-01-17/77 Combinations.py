class Solution:
    def combine(self, n, k):
        res = []
        path = []
        self.dfs(res, path, k, n, 1)
        return res
    
    def dfs(self, res, path, k, index):
        # stop condition
        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(index, n+1):
            path.append(i)
            self.dfs(res, path, k, n, i+1)
            path.pop()

    