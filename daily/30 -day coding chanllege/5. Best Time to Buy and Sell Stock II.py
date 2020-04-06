class Solution:
    def maxProfit(self, prices):
        low, high = 0, 0
        res = 0
        nums = prices
        while low < len(nums) - 1 and high < len(nums) - 1:
            while low + 1 < len(nums) and nums[low] >= nums[low+1]:
                low += 1
            high = low
            while high + 1 < len(nums) and nums[high] <= nums[high+1]:
                high += 1
            res += nums[high] - nums[low]
            low = high
        
        return res

# time complexity o(n)  --> only go through once
# space complexity o(1)

