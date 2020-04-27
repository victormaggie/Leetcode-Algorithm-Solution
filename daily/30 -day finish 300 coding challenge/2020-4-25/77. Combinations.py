class Solution:
    def combine(self, n, k):
        res, temp = [], []
        idx = 1
        self.dfs(res, temp, idx, n, k)
        return res
    
    def dfs(self, res, temp, idx, n, k):
        if len(temp) == k:
            res.append(temp[:])
            return
        for i in range(idx, n+1):
            temp.append(i)
            self.dfs(res, temp, i+1, n, k)
            temp.pop()

# time complexity o(k * Ckn)
# space complexity o(k + Ckn)


class Solution:
    def combine(self, n, k):
        nums = list(range(1, k+1)) + [n+1]
        output, j = [], 0
        while j < k:
            output.append(nums[:k])
            j = 0
            while j < k and nums[j+1] == nums[j] + 1:
                nums[j] = j + 1
                j + 1
            nums[j] += 1
        return output

# time complexity o(k*Ckn)
# space complexity o(k + Ckn)

