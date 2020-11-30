class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        if not board or not board[0]: return []
        if not words: return []
        
        m, n = len(board), len(board[0])
        res = set()
        for word in words:
            for i in range(m):
                for j in range(n):
                    # here check the word
                    self.dfs(board, m, n, i, j, 0, word, res)

        return list(res)
    
    def dfs(self, board, m, n, i, j, idx, word, res):
        # edge check
        # iterate all the numbers
        
        if board[i][j] != word[idx]: return
        
        if idx == len(word)-1: 
            print(word)
            res.add(word)
            return
        
        # left and right
        dx = (0, -1, 0, 1)
        dy = (-1, 0, 1, 0)
        
        tmp = board[i][j]
        board[i][j] = '.'
        for k in range(4):
            a = i + dx[k]
            b = j + dy[k]
            if a >= 0 and a < m and b >= 0 and b < n:
                self.dfs(board, m, n, a, b, idx+1, word, res)

        board[i][j] = tmp
                
# We need use trie tree for the solution

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    
        