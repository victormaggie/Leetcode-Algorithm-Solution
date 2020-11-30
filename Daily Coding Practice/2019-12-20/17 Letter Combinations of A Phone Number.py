class Solution:
    def letterCombinations(self, digits):
        hash_table = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        stack = []
        for i in digits:
            stack.append(hash_table[int(i)])

        res = []
        path = ''
        idx = 0
        self.dfs(stack, idx, res, path)
        return res
    
    def dfs(self, stack, idx, res, path):
        if not stack:
            return
        if idx == len(stack):
            res.append(path)
            return
        for j in range(len(stack[idx])):
            self.dfs(stack, idx+1, res, path+stack[idx][j])

# time complexity  --> 4^n
# space complexity --> o(n)
