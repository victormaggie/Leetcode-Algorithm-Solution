class Solution:
    def mySqrt(self, x):
        if x == 0 or x == 1: return x
        return int(10 ** (0.5 * math.log10(x)))


class Solution:
    def mySqrt(self, x):
        if x < 2: return x
        left, right = 2, x //2
        while left <= right:
            mid = left + (right - left) //2
            num = mid **2
            if num > 2:
                right = mid -1
            elif num < x: left = mid + 1
            else: return mid
        # be aware that we need to return right --->
        # this is the jump out value !!
        return right

# time complexity o(logn)
# space complexity o(1)
