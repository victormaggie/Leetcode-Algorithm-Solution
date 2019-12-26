class Solution(object):
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 1
        self.memo[1] = 1
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # choice
        # use memorization
        if n in self.memo:
            return self.memo[n]
        steps = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = steps
        return steps

# dynamic programming

class Solution2(object):
    
    def climbStairs(self,n):
        stack = [0] * (n+1)
        stack[0] = 1
        stack[1] = 1
        for i in range(2, n+1):
            stack[i] = stack[i-1] + stack[i-2]
        return stack[-1]