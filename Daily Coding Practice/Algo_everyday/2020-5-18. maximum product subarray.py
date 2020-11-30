class Solution:
    def maxProduct(self, nums):
        min_num = 1
        max_num = 1
        res = -float('inf')

        for i in nums:
            if i < 0:
                # swap the max and min
                max_num = min_num
                min_num = max_num
            
            max_num = max(max_num *i, i)
            min_num = min(min_num *i, i)
            res = max(max_num, res)
        return res
    
# time complexity o(n)
# space complexity o(1)
