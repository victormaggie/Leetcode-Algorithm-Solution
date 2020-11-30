class Solution:
    def minconstTickets(self, days, costs):
        dp = [0] * (days[-1] + 1)
        for i in range(1, len(dp)):
            if i not in days:
            # this is o(n) find need to optimize
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[max(0, i-1), cost[0]],
                    dp[max(0, i-7), cost[1]],
                    dp[max(0, i-30), cost[2]]
                )
        return dp[-1]
# time compelxity o(N^2)
# space complexity o(N)


    def minconstTickets(self, days, costs):
        dp = [0] * (days[-1] + 1)
        idx = 0
        for i in range(1, len(dp)):
            if i != days[idx]:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[max(0, i-1), cost[0]],
                    dp[max(0, i-7), cost[1]],
                    dp[max(0, i-30), cost[2]]
                )
        return dp[-1]

# time complexity o(N)
# space complexity o(N)

