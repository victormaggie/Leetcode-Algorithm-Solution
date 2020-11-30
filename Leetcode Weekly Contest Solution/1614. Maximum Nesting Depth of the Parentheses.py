class Solution:
    def maxDepth(self, s):
        ans = 0
        bal = 0

        for i in s:
            if i == '(': bal += 1
            if i == ')': bal -= 1
            if ans < bal: ans = bal
        return ans

# o(n)
# o(1)
