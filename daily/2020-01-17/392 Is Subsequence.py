class Solution:
    def isSubsequence(self, s, t):
        s = list(s)
        for c in t:
            if not s: return True
            if c == s[0]:
                s.pop(0)
        return not s

    
    # binary search solution give to tomorrow!
    