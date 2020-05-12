class Solution:
    def myPow(self, x, n):
        # if we use the brute force solution
        # time complexity will be o(n)


        # use divide and conquer solution
        # binary split
        # time complexity will be o(logn)
        if x == 0.0: return 0.0
        res = 1
        # think about the negative situation
        if n < 0: x, n = 1/x, -n
        while n:
            if n & 1:  # the odd number
                res *= x
            x *= x
            n >>= 1
        return res
    
    # time complexity o(logn)
    # space complexity o(1)
    
