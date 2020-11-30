class Solution:
    def removeElement(self, nums, val):
        left, right, end = 0, len(nums)-1, len(nums)-1
    
        while left <= end:
            if nums[left] == val:
                nums[left], nums[right], end = nums[end], nums[left], end-1
            else:
                left += 1
        
        return left

    # the two point solution is good, but it did not remove the nums list

    # I think if we use the remove function if will be better

    def removeElement1(self, nums, val):
        while True:
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)

        
