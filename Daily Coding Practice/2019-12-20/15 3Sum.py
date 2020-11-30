class Solution:
    def threeSum(self, nums):
        import itertools
        # use the recursion tree solution
        #nums = list(set(nums))
        #print(nums)
        res = []
        path = []
        idx = 0        
        self.dfs(nums, res, idx, path)
        res.sort()
        return list(k for k,_ in itertools.groupby(res))
    
    def dfs(self, nums, res, idx, path):
        #print(path)
        # stop condition
        if len(path) == 3:
            if sum(path) == 0:
                res.append(sorted(path[:]))
                return
            return
        
        # traversal the sum
        #for i in range(len(nums[idx:])):        
        for start in range(idx, len(nums)):
            self.dfs(nums, res, start+1, path + [nums[start]])
            # path = []

# time complexity is not good
# we need use the two pointer