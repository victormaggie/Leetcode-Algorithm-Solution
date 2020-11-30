class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        x1 = 0
        for i in range(n+1):
            x1 ^= i
        for i in nums:
            x1 ^= i
        return x1

# time complexity o(N)
# space complexity o(1)

