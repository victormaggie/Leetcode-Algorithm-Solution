
# DP solution

class Solution:
    
    def numRollsToTarget(self, d, f, t):
        
        # edge case here
        
        mod = 10 ** 9 + 7
        
        if d * f < t: return 0
        
        if d * f == t: return 1
        
        dp = [[0 for _ in range(t+1)] for _ in range(d+1)]
        
        # initialization
        
        for j in range(1, min(f+1, t+1)): dp[1][j] = 1
        
        for i in range(2, d+1):
            for j in range(2, t+1):
                for k in range(1, f+1):
                    # unbounded backpack, means we still can carrier this value
                    if j - k >= 0: dp[i][j] += dp[i-1][j-k]
            
                dp[i][j] %= mod
        
        return dp[-1][-1]