class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # This is a typical unbounded dynamic programming questions.
        # 2 dimension DP
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]

        for i in range(len(coins))
            for j in range(1, amount):
                if i > 0: dp[i][j] = dp[i-1][j]
                if j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]]
        
        return dp[-1][-1]

# time complexity (o(nxm))
# space complexity o(nxm)
