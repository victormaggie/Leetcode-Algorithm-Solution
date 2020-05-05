class Solution:
    def singleNumber(self, nums):
        bitwise = 0
        for i in nums:
            bitwise ^= i
        
        diff = bitwise & (-bitwise)
        res = [0, 0]
        for i in nums:
            if diff & i:
                res[0] ^= i
            else: res[1] ^= i
        return res

# time complexity o(N)
# space complexity o(1)
