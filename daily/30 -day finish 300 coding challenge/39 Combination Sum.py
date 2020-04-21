class Solution:
    def combinationSum(self, candidates, target):
        # we need to sort the array, otherwise it will have another issue
        candidates = sorted(candidates)
        res = []
        temp = []
        self.dfs(candidates, res, temp, 0, target)
        return res

    def dfs(self, candidates, res, temp, idx, target):
        if target < sum(temp):
            return
        # here we can optimize the solution
        # update the target --> 
        if target == sum(temp):
            res.append(temp[:])
            return

        for i in range(idx, len(candidates)):
            temp.append(candidates[i])
            self.dfs(candidates, res, temp, i, target)
            temp.pop()

# dfs --> backtracking

class Solution:
    def combinationSum(self, candidates, target):
        candidates = sorted(candidates)
        res = []
        temp = []
        self.dfs(candidates, res, temp, idx, target)
        return res
    def dfs(self, candidates, res, temp, idx, target):
        if target < 0:
            return
        if target == 0:
            res.append(temp[;])
            self.dfs(candidates, res, temp, i, target)
            temp.pop()

## 2020-04-20

