class Solution:
    def singleNumber(self, nums):
        bitwise = 0
        for i in nums:
            bitwise ^= i
        # we have to use the lowbit to split the data!
        lowbit = bitwise & (-bitwise)
        x = 0 
        for i in nums:
            if lowbit & i:
                x ^= i
        return [x, x ^ bitwise]

# time complexity o(N)
# space complexity o(1)