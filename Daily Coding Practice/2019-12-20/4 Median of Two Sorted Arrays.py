import math
class Solution:
    def findMedianSortedArray(self, nums1, nums2):
        # thoughts combine the array
        # find the median value of the calculation

        if not nums1 and nums2:
            return
        
        num = sorted(nums1 + nums2)
        idx = len(num)

        if idx % 2 == 0: 
            median = (num[idx//2] + num[idx//2-1]) / 2
            return median
        else:
            return num[math.floor(idx//2)]

