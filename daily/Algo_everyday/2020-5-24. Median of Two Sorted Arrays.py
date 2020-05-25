from typing import List

class Solution:
    def findMedianSortedArray(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2: return 

        # do a swap and save the time!
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        start = 0
        end = m

        left_total = (m + n + 1) >> 1

        while start <= end:
            partition1 = (start + end) >> 1
            partition2 = left_total - partition1

            # boundary check 
            nums1_left_max = float('-inf') if partition1 == 0 else nums1[partition1-1]
            nums1_right_min = float('inf') if partition1 == m else nums1[partition1]

            nums2_left_max = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            nums2_right_min = float('inf') if partition2 == n else nums2[partition2]

            if nums1_left_max