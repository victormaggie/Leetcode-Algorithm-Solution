class Solution(object):
    def longthOfLIS(self, nums):
        if not nums: return 0
        dp = [1] * len(nums)
        i = 1
        while i < len(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            i += 1

        return max(dp)
# time complexity o(n^2)
# space complexity o(n)

    def longthOfLIS2(self, nums):
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
