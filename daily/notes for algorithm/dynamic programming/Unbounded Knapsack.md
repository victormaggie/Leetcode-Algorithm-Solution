### Unbounded knapsack

Unbounded kanpsack is a problem related to the question how many way or least steps etc, there is unbound quantity, when solve this kind of problems, we should first figure out it is 1 dimension DP or 2 dimension DP.

  * Given the weights and profits of 'N' items, we are asked to put these items in a knapsack which has a capcity C. the goal is to get `maximum` profit from the items in the knapsack. 

 * I. Examples for the unbounded knapsack
   * Carry some fruits in the knapsack to get the **maximum** profit.
     * Items: {Apple, Orange, Melo}
     * Weights: {1, 2, 3}
     * Profit: {15, 20, 50}
     * Knapsack capacity: 5
   * Brute force solution 
        ```
            def knapsack(profits, weights, capacity): 
                return knapsack_recursive(profits, weights, capacity, 0)
            
            def knapsack_recursive(profits, weights, capacity, currentIndex):
                n = len(profits)
                if capacity <= 0 or n == 0 or len(weights) != n or currentIndex >= n:
                    return 0
                
                profit1 = 0
                if weight[currentIndex] <= capacity:
                    # case 1 recursive call with the current weight
                    profit1 = profits[currentIndex] + knapsack_recursive(profits, weights, capacity - weights[currentIndex], currentIndex)
                
                # case 2 recursive call without the current weight
                profit2 = knapsack_recursive(profits, weights, capacity, currentIndex+1)

                return max(profit1, profit2)

        ```
        The brute force will ETL due to a lot of duplicate calculation in the equations.
    * Top down method with memozaition
        This is a 2 dimension DP question, the row is currentIndex, the columns is the weight, we use the DP array to memorize the calculated results.
        ```
        def knapsack(profits, weights, capacity):
            dp = [[-1 for i in range(capacity + 1)] for j in range(len(weights))]
            return knapsack_recursive(profits, weights, capacity, 0)
        
        def knapsack_recursive(profits, weights, capacity, currentIndex):
            n = len(profits)
            if n == 0 or capacity <= 0 or len(weights) != n or currentIndex >= n:
                return 0
            
            if dp[currentIndex][capacity] != -1: return dp[currentIndex][capacity]

            if dp[currentIndex][capacity] == -1:
                profit1 = 0
                if weigth[currentIndex] <= capacity:
                    # case I: knapsack this value
                    # **be aware of that: Here we can use the duplicate number so the index will not increase, still currentIndex**
                    profit1 = profit[currentIndex] + knapsack_recursive(profits, weights, capacity - weight[currentIndex], currentIndex)
                profit2 = knapsack_recursive(profits, weights, capacity, currentIndex + 1)
                
                dp[currentIndex][capacity] = max(profit1, profit2)
            
            return dp[currentIndex][capacity]
        ```
        **Be aware of that** : Inside the recursion function, the index did not increase a lot.

    * Bottom up method with dp array

        ```
        def knapsack(profits, weights, capacity):
            if not weights or not profits: return 0
            if capacity == 0: return 0
            # define the dp array
            dp = [[0 for i in range(capacity + 1)] for j in range(len(weights))]
            for i in range(len(weights)):
                for c in range(1, capacity + 1):
                    # dp restore the maximum nums, which one is larger --> 
                    # knapsack or un-knapsack
                    profit1, profit2 = 0, 0
                    # case 1: pack the current one
                    if weights[i] <= c:
                        profit1 = profits[i] + dp[i][c - weights[i]]
                    # case 2: unpack the current one
                    profit2 = dp[i-1][c]
                    
                    dp[i][c] = max(profit1, profit2)
            return dp[-1][-1]
        ````

*   II. Example 2: cutting rod
    *   Given a rod of length 'n', we are asked to cut the rod and sell the pieces in a way that will maximize the profit.
        *   Length: [1, 2, 3, 4, 5]
        *   Prices: [2, 6, 7, 10, 13]
        *   Rod Length: 5
    * Brute force solution
       ```
        def cut_rod(profits, length, total_length):
            return cut_rod_recursive(profits, length, total_length, 0)
        
        def cut_rod_recursive(profits, length, total_length, currentIndex):
            # stop condition
            n = len(length)
            if currentIndex >= len(length) or n == 0 or total_length <= 0:
                return 0
            
            # case 1: recursive solve add current value
            profit1 = profits[currentIndex] + cut_rod_recursive(profits, length, total_length - length[currentIndex], currentIndex)

            # case 2: recursive solve does not add current profit
            profit2 = cut_rod_recursive(profits, length, total_length, currentIndex+1)
        
            return max(profit1, profit2)
       ```
    
    * Top down with memozaition solution

    ### do it later


    * Bottom up solution with dp array
        ```
        def cut_rod(profits, length, total_length):
            # edge case check
            n = len(length)
            if  n == 0 or not profits:
                return 0
            dp = [[0 for i in range(total_length+1)] for j in range(n)]
            for i in range(n):
                for c in range(1, total_length):
                    if c >= weight[i]:
                        dp[i][c] = max(profits[i] + dp[i][c - length[i]], dp[i-1][c])
                    else:
                        dp[i][c] = dp[i-1][c]

            return dp[n-1][total_length] 
        ```
