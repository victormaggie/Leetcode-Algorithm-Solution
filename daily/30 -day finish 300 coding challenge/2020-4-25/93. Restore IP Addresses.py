class Solution:
    def restoreIpAddresses(self, s):
        if len(s) > 12:
            return []
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, path, res):
        if len(s) > (4 - len(path)) * 3:
            return 
        
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        
        for i in range(1,4):
            if i > len(s):
                continue
            number = int(s[:i])
            if str(number) == s[:i] and number <= 255:
                self.dfs(s[i:], path + [s[:i]], res)

########
