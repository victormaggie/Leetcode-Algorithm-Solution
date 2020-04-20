class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            # divide and conquer solution
            if nums[mid] == target:  # case I
                return mid
            elif nums[mid] <= nums[-1]:  # case II --> right --> continuous
                if target > nums[mid] and target < nums[-1]:
                    left = mid + 1
                else:
                    right = mid -1 
            elif nums[mid] >= nums[0]:  # case III --> left --> continuous
                if target > nums[0] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
