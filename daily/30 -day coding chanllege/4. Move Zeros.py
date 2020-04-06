class Solution:
    def moveZeros(self, nums):
        # Do not return anything, modify nums in-place instead
        fast = 0
        slow = 0

        while fast < len(nums) - 1:
            if nums[fast] != 0 and nums[slow] != 0:
                fast += 1
                slow += 1
            
            elif nums[fast] == 0 and nums[slow] == 0;
                while nums[fast] == 0 and fast < len(nums) - 1:
                    fast += 1
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1

# time complexity o(n^2)
# space complexity o(1)

