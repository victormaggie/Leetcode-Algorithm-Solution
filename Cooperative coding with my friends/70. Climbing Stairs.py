class Solution(object):

    def climbStairs(self, n):

        # fibonacci sequence question
        a = 1
        b = 1

        for i in range(n-1):
            a, b = a+b, a
        return a
    
    