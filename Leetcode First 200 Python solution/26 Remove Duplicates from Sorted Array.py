
# Remove Duplicates from Sorted Array

class Solution:
	def removeDuplicates(self, nums):
		
        if not nums: return 0
        
        k = 0
        for i in range(0, len(nums)):
            if not i or nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

# o(n) solution here
# o(1) space complexity

