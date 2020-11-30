# This is the typical dynamic programming questions
# split the question as ---> steal current, then idx move forward 2
# split the question as ---> skip current, then the idx will move 1

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dfs(nums, 0)
    
    def dfs(self, nums, idx):
        if idx >= len(nums): return 0
        stealCurrent = nums[idx] + self.dfs(nums, idx+2)
        skipCurrent = self.dfs(nums, idx+1)
        return max(stealCurrent, skipCurrent)

# Brute force solution: o(2^2)
# space complexity: o(n)

# we use the DP memozaition solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or sum(nums) == 0: return 0
        dp = [0 for i in range(len(nums))]
        return self.dfs(nums, dp, 0)
    
    def dfs(self, nums, dp, idx):
        # stop condition
        if idx == len(nums):
            return 0
        
        if dp[idx] == 0:
            stealCurrent = nums[idx] + self.dfs(nums, dp, idx + 2)
            skipCurrent = self.dfs(nums, dp, idx + 1)
            dp[idx] = max(stealCurrent, skipCurrent)
        return dp[idx]

# time complexity o(n)
# space complexity o(n)


# we use the bottom up solution for the calculation
class Solution:
    def rob(self, nums: List[int]) -> int:
        # considering the edge case
        if not nums: return 0
        if len(nums) == 1: return nums[-1]
        if len(nums) == 2: return max(nums[0], nums[1]) 

        # use the bottom up solution for the calculation
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        dp = [0 for x in range(n+1)]
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, n):
            dp[i+1] = max(nums[i] + dp[i-1], dp[i])
        return dp[n]


# optimize the memory 
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0

        n1, n2 = 0, nums[0]
        for i in range(1, n):
            n1, n2 = n2, max(n1+nums[i], n2)
        return n2
