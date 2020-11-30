class Solution(object):
    def longestValidParenthese(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = []
        start, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                q.append(i)
                continue
            # here is the ')'
            # if stack is None --> index more to i
            if not q:
                start = i + 1
            else:
                q.pop()
                ans = max(ans, i - q[-1] if q else i - start + 1)
        return ans

        