class Solution:
    # back-tracking

    def partition(self, s):
        res = []
        temp = []
        self.dfs(s, temp, res)
        return res
    def dfs(self, s, temp, res):
        # return condition
        if not s:
            return res.append(temp[:])

        # back-tracking
        for i in range(1, len(s)+1):
            if self.isPalis(s[:i]):
                temp.append(s[:i])
                self.dfs(s[i:], temp, res)
                temp.pop()

    def isPalis(self, s):
        return s == s[::-1]

# time complexity o(n * 2^n)
# space complexity o(n)
