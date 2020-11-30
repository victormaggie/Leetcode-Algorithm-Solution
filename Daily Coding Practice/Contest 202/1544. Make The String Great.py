class Solution:
    def makeGood(self, s:str) -> str:
        if not s: return ''

        stack = []
        for i in s:
            if not stack or abs(ord([-1]) - ord(i)) != 32:
                stack.append(i)
                continue
            else:
                stack.pop()
        return ''.join(stack)

# time complexity o(n)
# space complexity o(n)

