
# order
# 

from itertools import permutations

class Solutions1:
    def permute(self, nums):
        return list(permutations(nums))

class Solutions2:
    def permute(self, nums):
        
        res = []
        self.dfs(nums, res, [])
        return res
    
    def dfs(self, nums, res, path):
        if not nums:
            res.append(path)
        
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], res, path + [nums[i]])

class Solutions3:
    def permute(self, nums):

        visited = [0] * len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path+[nums[i]])
                        visited[i] = 0  # back-tracking
        dfs([])
        return res


from itertools import permutations
class Solution5:
    def permute(self, nums):
        
        # return list(permutations(nums))
    
    
        # back-tracking problem
        
        visited = [None] * len(nums)
        res = []
        path = []
        ans = []
     
        def dfs(nums, res, path, visited, ans):

            if len(path) == len(nums):
                res.append(path)
                ans.append(path)
                print(path)
                return
            else:
                for i in range(len(nums)):
                    if visited[i] == None:
                        visited[i] = True
                        path.append(nums[i])
                        dfs(nums, res, path, visited, ans)
                        path.pop()
                        visited[i] = None

        dfs(nums, res, path, visited, ans)

        return ans


class Solution4:
    def permute(self, nums):
        
        # return list(permutations(nums))
    
    
        # back-tracking problem
        
        visited = [None] * len(nums)
        res = []
        path = []
        self.dfs(nums, res, path, visited)
        return res
        
        
    def dfs(self, nums, res, path, visited):
        
        if len(path) == len(nums):
            res.append(path)
            return
        else:
            for i in range(len(nums)):
                if visited[i] == None:
                    visited[i] = True
                    path.append(nums[i])
                    self.dfs(nums, res, path, visited)
                    path.pop()
                    visited[i] = None
