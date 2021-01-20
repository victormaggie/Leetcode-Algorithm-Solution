
# Count the vowel strings

class Solution:
    def countVowelStrings(self, n):
        
        ans = 0
        
        def dfs(n, cnt, idx):
            nonlocal ans
            
            if n == cnt:
                ans += 1
                return
            
            for i in range(idx, 5):
                dfs(n, cnt+1, i)
        
        dfs(n, 0, 0)
        return ans
        
# n ^ 5  time complexity

# backtracking is a general approach that works by identifying potential
# candidates and incrementally builds using depth first search. once the required goal is reached
# we explore the others.

# Memorization

class Solution:
    def countVowelStrings(self, n):
        
        dp = [[0 for i in range(n)] for j in range(6)]
        
        for i in range(6):
            dp[i][0] = 1
        
        m = 5
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]


class Solution:
    def countVowelString(self, n):
        
        dp = [[0 for i in range(n)] for j in range(6)]
        
