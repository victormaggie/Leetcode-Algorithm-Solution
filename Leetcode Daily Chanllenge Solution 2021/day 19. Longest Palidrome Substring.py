
# Longest Palindrome Substring

# the most brutal force solution

class Solution:
    
    def brute_force(self, s):
        
        if len(s) <= 1: return s
        
        ans = ''
        
        for i in range(len(s)):
            for j in range(0, i+1):
            
                if s[j:i+1] == s[j:i+1][::-1]:
                    
                    if len(ans) < i - j + 1: ans = s[j:i+1]
                    break
        
        return ans

# o(n^3) solution, here the reverse string is o(n), and iterate twice string! 


    def middel_spreed(self, s):
        
        ans = ''
        
        # iterate all the index
        for i in range(len(s)):
            
            ans1 = self.check(s, i, i)
            if len(ans) < len(ans1): ans = ans1
            ans2 = self.check(s, i, i+1)
            if len(ans) < len(ans2): ans = ans2

        return ans
   
    def check(self, s, i, j):
        
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
            
        return s[i+1: j]
    
    
    def dynamic_programming(self, s):
        
        # dynamic programming
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        # calculate the solution as it 
        
        n = len(s)
        
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        ans = ''
        maxLen = 0
        
        # the end index
        for j in range(n):
        # the starting index
            for i in range(0, j+1):
            # current index can be put there
                if s[i] == s[j]:
                    # the index is close here!
                    if j - i <= 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if maxLen < j - i + 1:
                            maxLen = j - i + 1
                            ans = s[i: j + 1]
        return ans
                    
# o(n^2) solution, and here we use o(n^2) space complexity 

        
        