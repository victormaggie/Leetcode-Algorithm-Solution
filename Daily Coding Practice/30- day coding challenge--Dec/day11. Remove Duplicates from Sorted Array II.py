
# Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums):
        k = 0
        count = 0
        
        for i in range(len(nums)):
            
            if not i or nums[i] != nums[k-1]:
                count = 0
            
            if count < 2:
                nums[k] = nums[i]
                k += 1
                count += 1
        
        return k

# o(n) solution

