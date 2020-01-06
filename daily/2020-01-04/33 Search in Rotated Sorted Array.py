class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[m] >= nums[0] and (nums[0] <= target < nums[m]):
                r = m - 1
            elif nums[m] >= nums[0]:
                l = m + 1
            elif nums[m] < nums[0] and (nums[m] < target <= nums[-1]):
                l = m + 1
            else:
                r = m - 1
        return -1

