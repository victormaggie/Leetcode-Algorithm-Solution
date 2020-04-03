# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# output 6

class Solution:
    def maxSubArray(self, nums):
        # dynamic programming
        dp = [-float('inf')]
        for i in range(len(nums)):
            dp.append(max(dp[i]+nums[i], nums[i]))
        return max(dp)

    # time complexity o(n)
    # space complexity o(n)

    def maxSubArray(self, nums):
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum

# time complexity o(n)
# space complexity o(1)


    