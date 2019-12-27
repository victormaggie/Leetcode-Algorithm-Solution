class Solution:

# binary search solution
    def searchInsert(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0
        
        left, right = 0, len(nums)-1
        # the left need smaller than the right
        while left <= right:
            # remember here is add
            mid = (right + left)//2
            if nums[mid] == target:
                # if found
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Brute force solution
    def searchInsert2(self, nums, target):
        if target > nums[-1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

# time complexity o(n)