class Solution:
    def letterCasePermutation(self, S):
        
        # use BFS to solve this problem
        res = [[]]
        
        for i in S:
            if i.isalpha():
                n = len(res)
                for j in range(n):
                    res.append(res[j][:])
                    res[i].append(i.lower())
                    res[n+i].append(i.upper())
            else:
                for j in res:
                    j.append[i]

        return list(map(''.join, res))

# time complexity o(N*2^N)
# space complexity o(2^N)

# recursion solution
class Solution:
    def letterCasePermutation(self, S):
        res = []
        temp = ''
        self.dfs(S, res, temp, 0)
        return res
    
    def dfs(self, S, res, temp, idx):
        if idx == len(S):
            res.append(temp)
            return
        if S[idx].isalpha():
            self.dfs(S, res, temp+S[idx].upper(), idx+1)
            self.dfs(S, res, temp+S[idx].lower(), idx+1)
        else:
            self.dfs(S, res, temp+S[idx], idx+1)

# time complexity o(N*2^N)
# space complexity o(2^N)

class Solution:
    def letterCasePermutation(self, S):
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))

# time complexity o(N * 2^N)
# space complexity o(2^N)



