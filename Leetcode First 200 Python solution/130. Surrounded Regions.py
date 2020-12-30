class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        # be sure of the edge case
        if not board or not board[0]: return None
        
        # use dfs solution to calcalte all the o connected to the ocean
        m, n = len(board), len(board[0])
        
        
        def dfs(board, i, j):
            
            if board[i][j] == 'X' or board[i][j] == '.':
                return
            
            board[i][j] = '.'
            
            # four direction here
            dx = (-1, 0, 1, 0)
            dy = (0, -1, 0, 1)
            
            for k in range(4):
                
                x = j + dx[k]
                y = i + dy[k]
                
                if 0 <= x < n and 0 <= y < m and board[y][x] == 'O':
                    # recursion ahead
                    dfs(board, y, x)
        
    
        # Step 2: iterate all the four border to the ocean
        
        for j in range(n):
            if board[0][j] == 'O': dfs(board, 0, j)
            if board[-1][j] == 'O': dfs(board, m-1, j)

        
        for i in range(m):
            if board[i][0] == 'O': dfs(board, i, 0)
            if board[i][-1] == 'O': dfs(board, i, n-1)
                
        
        for i in range(m):
            for j in range(n):
                
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '.': board[i][j] = 'O'
        
        return board