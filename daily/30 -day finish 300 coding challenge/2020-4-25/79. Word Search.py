class Solution:
    def exist(self, board, word):
        if not board or not board[0]: return
        if not word: return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, m, n, i, j, 0):
                    return True
        return False
    
    def dfs(self, board, word, m, n, idx):
        if board[i][j] != word[idx]: return False
        if idx == len(word)-1: return True

        dx = (0, -1, 0, 1)
        dy = (-1, 0, 1, 0)
        board[i][j] = '.'
        for k in range(4):
            a = i + dx[k]
            b = j + dy[k]
            if a >= 0 and a < m and b >= 0 and b < n and self.dfs(board, word, m, n, idx+1):
                return True
        # backtracking here!
        board[i][j] = word[idx]

        