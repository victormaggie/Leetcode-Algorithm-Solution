# this is a backtracking problem

class solution(object):
    def permutation(self, nums):
        res = []
        path = []
        self.dfs(nums, res, path)
        return res
    
    def dfs(self, nums, res, path):
        # condition
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.dfs(nums, res, path)
            path.pop()

    def permutationII(nums):
        import itertools
        return itertools.permutations(nums)


