class Solution(object):
    def generateParenthesis(self, n):

        res = []
        path = ""
        # choice
        left_bracket, right_bracket = n, n
        self.dfs(left_bracket, right_bracket, res, path)
        return res
    
    def dfs(self, left_bracket, right_bracket, res, path):
        # goal
        if left_bracket == 0 and right_bracket == 0:
            res.append(path)
            return
        
        # condition 1
        if (left_bracket > 0):
            self.dfs(left_bracket -1, right_bracket, res, path + '(')
        
        # condition 2
        if (left_bracket < right_bracket):
            self.dfs(left_bracket, right_bracket -1, res, path + ')')

