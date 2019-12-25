import collections

class Solution:
    # brute force solution
    # o(n^3)
    def subarraySum(self, nums, k):
        count = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)+1):
                sum = 0
                for idx in range(i, j):
                    sum += nums[idx]
                if sum == k:
                    count += 1
        return count


class Solution2:
    # prefix sum
    def subarraySum(self, nums, k):
        count = 0
        for i in range(0, len(nums)):
            prefixSum = 0
            for j in range(i, len(nums)+1):
                prefixSum += nums[j]
                if prefixSum == k:
                    count += 1
        return count

# o(n^2)

class Solution3:
    # prefixSum array
    def subarraySum(self, nums, k):
        if (nums == None or len(nums) == 0):
            return 0
        # define a map
        sums = collections.default(int)
        ans = 0
        sums[ans] = 1

        # local variable
        prefixSum = 0
        count = 0
        for i in range(0, len(nums)):
            prefixSum += nums[i]
            count += 1


