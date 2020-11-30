class solution:
    def subarraySum(self, nums, k):
        if not nums or not nums[0]: return
        count, res, cum_sum = {0:1}, 0, 0
        for i in nums:
            cum_sum += v
            res += count.get(cum_sum-k, 0)
            count[cum_sum] = count.get(cum_sum, 0) + 1
        return res

# prefix sum