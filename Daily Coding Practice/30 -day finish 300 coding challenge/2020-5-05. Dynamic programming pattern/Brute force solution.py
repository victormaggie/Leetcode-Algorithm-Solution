class Solution:
    def solve_knapsack(profits, weights, capacity):
        return knapsack_recursive(profits, weigths, capacity, 0)

    def knapsack_recursive(profits, weights, capacity, currentIndex):
        # base checks
        if capacity <= 0 or currentIndex >= len(profits):
            return 0
        
        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process this
        profit = 0
        if weights[currentIndex] <= capacity:
            profit1 = profits[currentIndex] + knapsack_recursive(
                profits, weights, capacity-weights[currentIndex], currentIndex+1
            )

        profit2 = knapsack_recursive(profits, weights, capacity, currentIndex+1)
        return max(profit1, profit2)
    
# time complexity o(2^n)
# space complexity o(2^n)
