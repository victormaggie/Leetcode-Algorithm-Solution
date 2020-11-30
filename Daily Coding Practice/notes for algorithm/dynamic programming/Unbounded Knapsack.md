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

* **Example III**: 
  * Given an infinite supply of 'n' coins denominations and a total money amount, we are asked to find the total number of distinct ways to make up that amount.
    * `Denomination: {1, 2, 3}`
    * `amount: 5`
    * `output: 5`

  *  Brute force solution:
        ```
        def coin_change(self, amount, coins):
            return coin_change_recursive(self, amount, coins, 0)

        def coin_change_recursive(self, amount, coins, currentIndex):
            # stop condition
            n = len(coins)
            # be aware that: here for count the value
            if amount == 0: return 1
            if n == 0 or amount <0  or currentIndex >= n:
                return 0
            
            # case 1: using current coin
            # we only need to count the number of coin here, we do not need to find the total sum
            c1 = 0
            if amount - coins[currentIndex] >= 0:
                c1 = self.coin_change_recursive(amount - coins[currentIndex], coins, currentIndex)
            # case 2: do not use current coin, and jump next
            c2 = self.coin_change_recursive(amount, coins, currentIndex+1)

            sum = c1 + c2
        
            return sum

        ```

  * Top down solution for the calculation

    Be aware of that, we do not need to get the total value, we only need to get the count, thus no need add coins[i].
    ```
    def coin_change(self, amount, coins):
        # define dp --> This is 2 dimension dp questions
        dp = [[-1 for i in range(amount + 1)] for j in range(len(coins))]
        return coin_change_recursive(self, dp, amount, coins, 0)
    
    def coin_change_recursive(self, dp, amount, coins, currentIndex):
        if amount == 0: return 1
        n = len(coins)
        if n == 0 or amount < 0 or currentIndex >= n: return 0
        if dp[currentIndex][amount] != -1: return dp[currentIndex][amount]

        c1 = 0
        if amount - coins[currentIndex] >= 0:
            c1 = self.coin_change_recursive(dp, amount - coins[i], coins, current_Index)
        c2 = self.coin_change_recursive(dp, amount, coins, currentIndex + 1)
        dp[currentIndex][amount] = c1 + c2

        return dp[currentIndex][amount]
    ```
  * Bottom up Dynamic programming
    ```
    def coin_change(self, amount, coins):
        dp = [[0 for i in range(amount+1)] for j in range(len(coins))]
        # be aware of that when amount = 0 , the number need be 1 --> like recursive solution above
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for i in range(len(coins)):
            for j in range(1, amount +1 ):
                if i > 0:
                    dp[i][j] = dp[i-1][j]
                if t >= coins[i]:
                    dp[i][j] = dp[i][j - coins[i]]
        return dp[n-1][amount]

    ```
* **Example IV: Minimum coin change**
  * Given an infinite supply of 'n' coin denominations and a total money amount, we are asked to find the minimum number of coins needed to make up that amount.
    * `1, 2, 3`
    * `amount: 5`
    * `output: 2`

# do it later