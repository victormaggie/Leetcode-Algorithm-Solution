class Solution:
    def solve_knapsack(profits, weights, capacity):
        dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
        return knapsack_recursive(dp, profits, weights, capacity, 0)


    def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
        # base case
        if capacity <= 0 or currentIndex >= len(profits):
            return 0
        
        # if we have already solved a similar problem, return the result from memory
        if dp[currentIndex][capacity] != -1:
            # Prune the element here
            return dp[currentIndex][capacity]

        # recursive call after choosing the element at the currentIndex
        # if the weight of element at currentIndex exceeds the capacity

        profit1 = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentInDEX] + knapsack_recursive(
                dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1
            )
        
        # recursive call after excluding the element at the currentIndex
        profit2 = knapsack_recursive(
            dp, profits, weights, capacity, currentIndex + 1
        )

        dp[currentIndex][capacity] = max(profit1, profit2)

        return dp[currentIndex][capacity]

    def print_selected_elements(dp, weights, profits, capacity):
        print("Selected weights are: ", end='')
        n = len(weights)
        totalProfit = dp[n-1][capacity]
        for i in range(n-1, 0, -1):
            if totalProfit != dp[i-1][capacity]:
                print(str(weights[i]) + '', end='')
                capacity -= weights[i]
                totalProfit -= profits[i]
        
        if totalProfit != 0:
            print(str(weights[0]) + ' ', end='')
        print()
# time complexity o(N*C)
# space complexity o(N*c)

