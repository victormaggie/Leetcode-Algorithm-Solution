class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t): s, t = t, s
        ns, nt = len(s), len(t)
        if nt - ns > 1: return False
        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]
        # here we consider a case that 'a' and ''
        return ns + 1 == nt

# time complexity o(n)
# space complexity o(n)   the slice operation will take o(n)

# Be aware of that if we use dynamic programming, it will ETL
# time complexity o(N * M) !!
class Solution:
    def isOndeEditDistance(self, s: str, t: str) -> bool:
        dp = [[0 for i in range(len(s)+1)] for j in range(len(t)+1)]

        # initialization for the calculation
        for i in range(len(s)+1):
            dp[0][i] = i
        
        for j in range(len(t)+1):
            dp[j][0] = j
        
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if s[j-1] != t[i-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                else:
                    dp[i][j] = dp[i-1][j-1]
        
        return dp[-1][-1]

# time complexity o(n*m)
# space complexity o(n*m)

