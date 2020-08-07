from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = collections.Counter(nums)

        res = []

        for i in count:
            if count[i] == 2: res.append(i)
        
        return res

# time complexity o(n)
# space complexity o(n)

    
    # we need solve this one in o(n) time complexity
    # we need solve this problem in o(1) space complexity

    def findDuplicates(self, nums: List[int]) -> List[int]:

        # o(n)
        i = 0
        n = len(nums)
        res = []

        while i < n:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                res.append(nums[i])
        
        return res
    
    