class Solution:
    def Solve_knapsack(weights, profits, capacity):

        # No. 1 check the size of the array
        if capacity <= 0 or n == 0 or len(weights) != n: return 0

        # No. 2 dynamic programming for the calculation
        dp = [[0 for i in range(capacity+1)] for j in range(len(weights))]

        # No. 3 Initialization for the dp array
        for i in range(0, len(weights)):
            dp[i][0] = 0
        
        for j in range(capacity):
            if j >= weights[0]:
                dp[0][j] = weights[0]
        
        # No. 4 state transition for the calculation
        for i in range(1, len(weights) ):
            for j in range(1, capacity + 1):
                backpack = 0
                un_backpack = 0
                if j - weights[i] >= 0:
                    backpack = profits[i] + dp[i-1][j - weights[i]]

                un_backpack = dp[i-1][j]

                # dp array maxization
                dp[i][j] = max(backpack, unbackpack)

        return dp[-1][-1]

# backpack the dynamic programming
# solve this solution --> Bottom up!

# time complexity o(N*C)
# space complexity o(N*C)

