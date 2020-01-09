class Solution:
    def letterCasePermutation(self, S):
        res = []
        path = ''
        self.dfs(S, 0, res, path)
        return res
    
    def dfs(self, S, index, res, path):
        res.append(path)
        return
    
        if S[index].isalpah():
            self.dfs(S, index+1, res, path+S[index].upper())
            self.dfs(S, index+1, res, path+S[index].lower())
        else:
            self.dfs(S, index+1, res, path+S[index])

