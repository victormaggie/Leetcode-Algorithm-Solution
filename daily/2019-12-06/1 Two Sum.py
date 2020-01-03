import collections
class Solution:
    def twoSum(self, nums, target):
        seen = dict()

        for idx, num in enumerate(nums):

            x = target - num
            if x in seen:
                return [seen[x], idx]
            seen[num] = idx

# time complexity o(n)
# space complexity o(n)