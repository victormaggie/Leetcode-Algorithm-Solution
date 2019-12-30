class Solution(object):
    def isPowerOfThree(self, n):
        import math
        return n > 0 and (math.log10(n)/math.log10(3)) % 1 == 0

    