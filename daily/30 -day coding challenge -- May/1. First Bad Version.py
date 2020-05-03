class Solution:
    def firstBadVersion(self, n):
        if isBadversion(1) == 1: return 1
        if not isBadVersion(1) and isBadVersion(2) == 2: return 2

        left, right = 1, n
        while left <= right:
            mid = left + (right - left)//2
            if mid - 1 >= 1 and isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid): right = mid - 1
            else: left = mid - 1
    
    # binary search o(logn)
    # space complexity o(1)
