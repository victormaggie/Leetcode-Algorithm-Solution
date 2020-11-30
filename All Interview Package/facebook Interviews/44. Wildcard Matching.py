class Solution:
    def isMatch(self, s, p):
        n, m = len(s), len(p)

        s = ' ' + s
        p = ' ' + p

        f = [[0 for i in rang(m+1)] for j in range(n+1)]
        f[0][0] = True

        for i in range(n+1):
            for j in range(1, m+1):
                if p[j] == '*':
                    f[i][j] = f[i][j-1] or i and f[i-1][j]
                else:
                    f[i][j] = (s[i] == p[j] or p[j] == '?') and i and f[i-1][j-1]
        return f[n][m]

# dynamic programming --> 