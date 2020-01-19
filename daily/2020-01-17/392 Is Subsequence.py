class Solution:
    def isSubsequence(self, s, t):
        s = list(s)
        for c in t:
            if not s: return True
            if c == s[0]:
                s.pop(0)
        return not s
    
    # binary search solution give to tomorrow!
    
    "abcd"
    "affsbcd"

class Solution2:
    def isSubsequence(self, s, t):
        
        idex = collections.defaultdict(list)
        for i, c in enumerate(t)


class Solution3:
    def isSubsequence(self, s, t):
        if not s:
            return True
        for i in s:
            res = t.find(i)
            if res == -1:
                return False
            else:
                # here is pretty slow
                t = t[res+1:]
        return True

# this solution is very efficient
class Solution5:
    def isSubsequence(self, s, t):
        k = 0
        for c in s:
            # if cannot find, return -1
            k = t.find(c, k) + 1
            if k == 0: return False
        return True

class Solution4:
    def isSubsequence(self, s, t):
        for i in range(0, len(s)):
            try:
                index = t.index(s[i])
            except ValueError:
                return False
        t = t[index+1:]
        return True

import re

class Solution6:
    def isSubsequence(self, s, t):
        for c in s:
            try: k = re.search(c, t).start()
            except: return False
            t = t[k+1:]
        return True
