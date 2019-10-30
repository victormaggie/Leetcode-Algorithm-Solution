# dfs function for the calculation

class Solution:
    def combine(self, n, k):
        
        res = []
        path = []
        self.dfs(path, res, 1, n, k)
        return res
    
    def dfs(self, path, res, start, n, k):
        
        if k == 0:
            
            res.append(path[:])
            return
        
        for i in range(start, n+1):
            path.append(i)
            self.dfs(path, res, i+1, n, k -1)
            path.pop()

# complexity o(n)