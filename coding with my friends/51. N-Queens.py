from typing import List

class Solution:
    def solveNQueen(self, n: int) -> List[List[str]]:
        res = []
        path = [['.'] * n for i in range(n)]

        col = [False] * n
        dg = [False] * 2 * n
        udg = [False] * 2 * n

        def dfs(x):
            if x == n:
                res.append(["".join(path[i]) for i in range(n)])

            for i in range(n):
                if not col[i] and not dg[x+i] and not udg[n-x+i]:
                    path[x][i] = 'Q'
                    col[i] = dg[x+i] = udg[n-x+i] = True
                    dfs(x+1)
                    path[x][i] = '.'
                    col[i] = dg[x+i] = udg[n-x+i] = False
        dfs(0)

        return res
    
# time complexity o(N! n*2)
# space o(n*2)

