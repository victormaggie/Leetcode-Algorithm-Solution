# dfs and back tracking

class Solution:
    def letterCasePermutation(self, S):
        
        res = []
        self.dfs(S, 0, res, "")
        return res
    
    def dfs(self, S, n, res, path):

        if n == len(S):
            res.append(path)
            return
        
        if S[n].isalpha():
            self.dfs(S, n+1, res, path+S[n].lower())
            self.dfs(S, n+1, res, path+S[n].upper())
        else:
            self.dfs(S, n, res, path+S[n])