from typing import List
import collections

class Solution:
    def maxSubArrayLen(self, nums: List[int], k:int) -> int:
        # prefix sum
        hashmap = collections.defaultdict(int)
        hashmap[0] = -1
        res, prefix_sum = 0, 0

        for idx, val in enumerate(nums):
            prefix_sum += val
            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = idx
            
            if prefix_sum - k in hashmap:
                res = max(res, idx - hashmap[prefix_sum -k])

        return res

# time complexity o(n)
# space complexity o(n)

if __name__ == "__main__":
    test = Solution()
    nums = [1, -1, 5, -2, 3]
    k = 3
    print(nums)
    print(test.maxSubArrayLen(nums, k))