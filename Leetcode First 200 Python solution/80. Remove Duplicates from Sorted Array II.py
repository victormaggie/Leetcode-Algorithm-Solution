
# Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        count = 0
        for i in range(len(nums)):
            
            if not i or not nums[i] != nums[i-1]:
                count = 0
            
            if count < 2:
                nums[i] = nums[i]
                count += 1
                k += 1
        return k

# time complexity o(n)
# space complexity o(1)

