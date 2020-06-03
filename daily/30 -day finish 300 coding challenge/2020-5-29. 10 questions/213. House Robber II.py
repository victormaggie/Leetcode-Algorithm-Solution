class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp memozaition for the calculation
        # use bottom up solution
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        r1, r2 = 0, nums[0]
        n1, n2 = 0, nums[1]

        for i in range(1, n-1):
            r1, r2 = r2, max(r1 + nums[i])
        
        for j in range(2, n):
            n1, n2 = n2, max(n2, n1 + nums[j])
        
        return max(r2, n2)

# time complexity o(n)
# space complexity o(1)
