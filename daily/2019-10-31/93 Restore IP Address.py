# given a string containing only digits, restore it by returning all possible valid IP address combination

# "25525511135"
# ["255.255.11.135", "255.255.111.35"]

# IP address has 4 digits, each is between 0 ~255, dot separate

class Solution:
    def restoreIpAddresses(self, s):
        res = []
        path = ''
        self.dfs(s, 0, 0, res, path)
        return res
    
    def dfs(self, string, n, k, res, path):
        """
        string: the original string
        n: the current index
        k: current number we have
        res: current solution
        path: current path
        """
        if n == len(string):
            if k == 4:
                res.append(path)
                return
        
        if k > 4:
            return
        
        if n < len(string)-1 and string[n] == '0': self.dfs(string, n+1, k+1, res, path+'.0' )
        else:
            for i in range(n, len(string)):
                t = t * 10 + string[i] - '0'
                if t < 256: self.dfs(string, i+1, k+1, res, path+str(t))
                if t > 256: break
        



