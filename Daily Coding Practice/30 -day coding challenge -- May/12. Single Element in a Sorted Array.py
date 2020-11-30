class solution:
    def singleNonDuplicate(self, nums):
        # brute for solution
        for i in range(0, len(nums) -2, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]

# time complexity o(N)
# space complexity o(1)

# we know that sorted array should have binary search solution 
# reduce the time complexity to o(logn)

# this is non-trival bug
class Solution:
    def singleNoneDuplicate(self, nums):
        