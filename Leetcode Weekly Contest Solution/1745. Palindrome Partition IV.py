class Solution:

	# the brute force solution cannot pass it
    def checkPartitioning(self, s: str) -> bool:
        
        n = len(s)
        
        def check(i, j):
            
            while i < j and s[i] == s[j]:
                i += 1
                j -= 1
            
            return i == j or s[i] == s[j]
            
        # o(n)
        for left in range(n-2):
            
            right = n - 1
            # o(n)
            while left < right:
                # o(n)
                if check(0, left) and check(right, n-1) and check(left+1, right-1):
                    return True

                elif check(0, left):
                    right -= 1

                else:
                    left += 1
            
        
        # o(n^3)
        return False
            
    
    def checkPartitioning(self, s) -> bool:
    
        # dynamic programming count the place can split to palidrome
        
        n = len(s)
        
        dp [[False] * len(s) for i in range(n)]
        
        for i in range(n):
            
            dp[i][i] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                
                if s[i] == s[j]:
                    
                    if j - i == 1 or dp[i+1][j-1]:
                        
                        dp[i][j] == True
        
        for i in range(0, n-2):
            for j in range(n-1, i, -1):
            
                if dp[0][i] and dp[i+1][j-1] and dp[j][n-1]:
                
                    return True
                    
        return False
        
# Time complexity o(n ^ 2)
        

        
        
        
        
        
        
        
        
        
                
            
        