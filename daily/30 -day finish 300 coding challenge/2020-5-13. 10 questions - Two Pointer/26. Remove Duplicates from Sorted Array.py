class Solution:
    def removeDuplicates(self, nums):
        if not nums: return 0
        i = 0
        if j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1

# time complexity o(n)
# space complexity o(1)
