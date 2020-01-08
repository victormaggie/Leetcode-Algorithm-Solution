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
        # result array
        res = []
        path = []
        self.dfs(stack,0, res, path)
        return res
    
    def dfs(self, stack, index, res, path):
        if not stack == None: return

        # stop condition
        if len(stack) == index:
            res.append(path)
            return
        # recursion
        for j in range(len(stack[index])):
            self.dfs(stack, index+1, res, path+stack[index][j])
        
