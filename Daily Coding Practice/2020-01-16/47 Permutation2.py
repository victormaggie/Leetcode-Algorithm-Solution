class Solution:
    def permuteUnique(self, nums):

        res = []
        path = []
        nums.sort()
        self.used = [False] * len(nums)
        self.dfs(nums, res, path)
        return res

    def dfs(self, nums, res, path):
        if len(nums) == len(path):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if self.used[i]: continue
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] == True: continue
            self.used[i] = True
            path.append(nums[i])
            self.dfs(nums, res, path)
            path.pop()
            self.used[i] = False

            