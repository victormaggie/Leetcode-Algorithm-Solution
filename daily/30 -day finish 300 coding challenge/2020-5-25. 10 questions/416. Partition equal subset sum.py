from typing import List

# The typical 1/0 knapsack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1: return False
        target = total_sum >> 1
        n = len(nums)
        dp = [[False for _ in range(target + 1)] for y in range(n)]

        # populate the sum = 0 column, as we can always have 0
        for i in range(n):
            dp[i][0] = True

        # populate the first row as the first value

        for i in range(target + 1):
            dp[0][i] = nums[0] == i
        
        # process all subsets for all sums
        for i in range(1, n):
            for j in range(1, target + 1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i-1][j-nums[i]]

        return dp[-1][-1]

# time complexity o(N*M)
# space complexity o(N*M)

# The brute force solution
def canPartition(nums):
    s = sum(nums)
    if s & 1: return False
    return canPartition_recursive(nums, s >> 1, 0)

def canPartition_recursive(nums, target, currentIndex):
    # base check
    if sum == 0:
        return True
    
    n = len(nums)
    if n == 0 or currentIndex >= n:
        return False
    
    # recursive call after choosing the number at the 'currentIndex'
    # if the number at the 'currentIndex' exceeds the sum, we cannot process 
    if num[currentIndex] <= sum:
        if canPartition_recursive(nums, sum-nums[currentIndex], currentIndex+1):
            return True
    
    # recursive after excluding the current value
    return canPartition_recursive(num, sum, currentIndex+1)

# time complexity(2^n) --> n number and each number can be pack or unpack!
# space complexity o(n) --> memory which will be used to store the recursion stack
# this cannot pass the test case! --> memozaition


# Top down solution using memozaition
def canPartition(nums):
    s = sum(nums)
    if s & 1: return False
    # be aware that here -1 cannot be replaced as False
    # otherwise it will change the return value

    dp = [[-1 for x in range((s>>1) + 1)] for y in range(len(nums))]
    return True if canPartition_recursive(dp, nums, s>>1, 0) == 1 else False

def canPartition_topdown(dp, nums, target, currentIndex):
    # base check
    if target == 0: return 1

    n = len(num)
    if n == 0 or currentIndex >= n:
        return 0

    if dp[currentIndex][target] == -1:
        # we did not calculate this
        if nums[currentIndex] <= target:
            if canPartition_recursive(dp, num, target - nums[currentIndex], currentIndex + 1) == 1:
                dp[currentIndex][target] = 1
                # here we have early stop --> this is much better
                return 1
        
        # did not pack
        dp[currentIndex][target] = canPartition_recursive(dp, nums, target, currentIndex+1)
    
    return dp[currentIndex][target]



########## The fastest solution ######### only cost 40 ms
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1: return False
        target = total_sum >> 1

        # This prune is very nice !!!
        # This prune solved all the issue
        if max(nums) > target: return
        nums.sort(reverse=True)
        return self.helper(nums, target, 0, 0)
    
    def helper(self, nums, target, index, current_value):
        if current_value == target:
            return True
        
        for i in range(index, len(nums)):
            # 
            if current_value + nums[i] == target:
                return True
            # 
            if current_value + nums[i] > target:
                continue
            # pack and 
            if helper(nums, target, i + 1, current_value + nums[i]):
                return True
        
        return True
    


