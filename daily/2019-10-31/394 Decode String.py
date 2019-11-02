# Given an encoded string, return its decoded string
# encoding rule is K, where the encoded string inside the square brackets it being repeated exactly k time

# we can use the queue to solve this questions!

class Solution:
    def decodedString(self, s):
        res = []
        path = []
        self.dfs(s, start, res, path)
        return res
    
    def dfs(self, s, start, res, path):

        if start == len(s):
            res.append(path)
            return
        
        if i.isnumeric():
            i * path
        
        if i i
