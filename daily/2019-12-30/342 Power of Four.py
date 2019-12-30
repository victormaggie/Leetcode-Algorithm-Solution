class Solution(object):
    def isPowerOfFour(self, num):
        import math
        return num > 0 and (4 ** (int(math.log(num, 4)))) == num
