class Solution(object):
    def maxSubArray(self, nums):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # dynamic programming
        # edge case 
        if len(nums) == 1:
            return nums[0]

        dp = [-float('inf')]

        for i in nums:
            dp.append(max(nums[i], dp[i]+nums[i]))
        
        return max(dp)

# time complexity o(n)
# space complexity o(1)



    
