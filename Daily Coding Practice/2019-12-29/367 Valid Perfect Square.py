class Solution(object):
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        left, right = 0, num-1

        while left <= right:
            mid = (left + right)//2
            if mid**2 < num:
                left = mid + 1
            elif mid**2 > num:
                right = mid - 1
            else:
                return True
        return False

# time complexity o(logN)
# space complexity o(1)

