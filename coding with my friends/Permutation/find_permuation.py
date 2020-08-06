class Solution:
    def find_permutations(self, nums):
        res = []
        self.dfs(nums, res, [])
        return res

    def dfs(self, nums, res, temp):
        if len(nums) == len(temp):
            res.append(temp[:])
            return 
        
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.dfs(nums, res, temp)
            temp.pop()
    

if __name__ == "__main__":
    test = Solution()
    arr = [1, 3, 5]
    res = []
    test.dfs(arr, res, [])
    print(res)