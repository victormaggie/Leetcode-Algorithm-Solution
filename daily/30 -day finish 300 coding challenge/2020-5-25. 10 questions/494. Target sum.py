from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(maxsize=20000)
        # the lru_cache size will have troumendous influence on the final result
        def dp(start, presum):
            if start == len(nums):
                return 1 if 0 + presum == S else 0
            return dp(start+1, presum+nums[start]) + dp(start+1, presum-nums[start])
        return dp(0, 0)

