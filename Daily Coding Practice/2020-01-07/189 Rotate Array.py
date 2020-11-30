class Solution:
    
    def rotate(self, nums):
        if not nums: return 
        if k == 0: return nums
        while k:
            new = nums.pop()
            nums[:] = [new] + nums
            k -= 1


