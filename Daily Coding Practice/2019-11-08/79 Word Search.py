# word search
# Given a 2D boad and a word

class Solution:
    def exist(self, board, word):
        
        # define the 
        # boundary check
        if not board or not board[0]:
            return False
        
        m, n = len(board), len(board[0])
        
        # search the beginning part
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, 0):
                    return True
                    # start the dfs search algorithm for the calculation
                                        
        return False
    
    def dfs(self, board,x, y, word, u):
        
        # direction
        dx = (-1, 0, 1, 0)    # left and right
        dy = (0 , 1, 0, -1)   # down and up
        
        # stop condition --> not the same
        if board[x][y] != word[u]: return False
        # stop condition --> all the same
        if u == len(word)-1: return True
        
        board[x][y] = '.'
        m, n = len(board), len(board[0])
        
        for i in range(0, 4):
            a = x + dx[i]
            b = y + dy[i]
            if a >= 0 and a < n and b >= 0 and b < m:
                if self.dfs(board, a, b, word, u+1):
                    return True
        board[x][y] = word[u]
        
        return False


class Solution1:
    def exist(self, board, word):
        
        # 2D board and a word, find if the word exists in the grid
        
        # the world can be constructed from letters of 
        
        # edge case
        if len(board) == 0 and len(board[0]) == 0: return False
        
        n, m = len(board), len(board[0])
        
        for i in range(n):   # rows
            for j in range(m):  # columns
                if board[n][m] == word[0]:
                    if self.dfs(board, i, j, word, 0):  # random walk
                        return True 
        return False
    
    # define dfs method
    def dfs(self, board, x, y, word, u):
        
        dx = (-1, 0, 1, 0) # up , right, down, left
        dy = (0, 1, 0, -1)
        
        n, m = len(board), len(board[0])
        
        if board[x][y] != word[u]: return False
        if (u == len(word)-1): return True   # random walk all the elements
        
        board[x][y] = '.'
        # random walk all direction
        for i in range(4):
            a = x + dx[i]   # up and down
            b = y + dy[i]   # left and right
            
            # in side the boundary
            if a >= 0 and a < n and b >=0 and b < m:
                if (self.dfs(board, a, b, word, u+1)):
                    return True
        
        board[x][y] = word[u]
        
        return False