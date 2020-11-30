# Dynamics programming
# 1 Dynamics 0/1 method  400 ms

class Solution:
    def canPartition(self, nums):

        nums_sum = sum(nums)
        if nums_sum %2 != 0: return False

        # Memerization matrix
        dp = [0] * (nums_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(nums_sum, -1, -1):
                if dp[j]:
                    dp[j+num] = 1
            if dp[nums_sum//2] == 1:
                return True
        return False

    # This solution is very very slow, after transfer to 1 D, because without break   800ms
    def canPartition_1(self, nums):
        nums_sum = sum(nums)
        if nums_sum %2 != 0: return False

        dp = [False] * (nums_sum + 1)
        dp[0][0] = True

        for num in nums:
            for j in range(nums_sum, nums-1, -1):
                dp[j] = dp[j-num] or dp[j]     # be sure that this cannot be "+", otherwise will transfer to integer
        
        if dp[nums_sum//2] == True:
            return True
        return False
