
class Solution:

    # no stop condition
    # use a global to contain all the path
    def subsets(self, nums):
        self.res = []
        temp = []
        self.dfs(nums, 0, temp)
        return self.res
    
    def dfs(self, nums, idx, temp):
        self.res.append(temp[:])
        for i in range(idx, len(nums)):
            temp.append(nums[i])
            self.dfs(nums, i+1, temp)
            temp.pop()

# time complexity o(n * n^2)
# space complexity o(2^n)

class Solution:
    
