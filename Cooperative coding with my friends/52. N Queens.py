class Solution:
    def totalNQueens(self, n: int) -> int:
        
        col = [False] * (n)
        dg = [False] * (2 * n)
        udg = [False] * (2 * n)
        
        return self.dfs(col, dg, udg, n, 0)
    
    
    def dfs(self, col, dg, udg, n,  idx ):
        
        # stop condition
        if idx == n:
            return 1
        
        res = 0
        for j in range(n):
        # backtracking here
            if not col[j] and not dg[n+idx-j] and not udg[idx+j]:
                col[j] = dg[n+idx-j] = udg[idx+j] = True
                res += self.dfs(col, dg, udg, n, idx + 1)
                col[j] = dg[n+idx-j] = udg[idx+j] = False
        
        return res

# time complexity o(N! )