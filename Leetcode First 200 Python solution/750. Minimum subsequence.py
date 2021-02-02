

class Solution:
    
    def minWindow(self, S, T):
        
        N = len(S)
        
        nxt = [None] * N
        
        last = [-1] * 26
        
        for i in range(N-1, -1, -1):
            
            last[ord(S[i]) - ord('a')] = i
            nxt[i] = tuple(last)
        
        windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
        
        for j in range(1, len(T)):
            
            letter_index = ord(T[j] - ord('a'))
            windows = [[root, nxt[i+1][letter_index]]
                
                for root, i in windows if 0 <= i < N-1 and nxt[i+1][letter_index] >= 0
            ]
            
        if not windows: return ""
        
        i, j = min(window, key = lambda (i, j): j - i)
        
        return S[i: j+1]
        