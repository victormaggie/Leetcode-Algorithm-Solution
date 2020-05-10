class Solution:
    def isPerfectSquare(self, num):
        if num < 2:
            return True
        
        left, right = 0, num//2
        while left <= right:
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            else:
                right = mid -1
        return False

# time complexity o(logn)
# space complexity o(1)