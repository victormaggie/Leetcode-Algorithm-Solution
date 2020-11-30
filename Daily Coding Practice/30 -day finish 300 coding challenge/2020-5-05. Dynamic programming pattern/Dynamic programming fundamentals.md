# Dynamic programming

* we use the memorization to reduce the repeative subarray calculation

* Example
  
```
  def knapsack_recursive(profits, weights, capacity, currentIndex):
    # stop condition
    if capacity <= 0 or currentIndex >= len(profits):
        return 0
    
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we shouldn't process
    profit =0 
    if weight[currentIndex] <= capacity:
        # select the current item
        profit1 = profits + knapsack_recursive(
            profits, weights, capacity - weights[currentIndex], currentIndex + 1
        )
        # did not select the current item
        profit2 = knapsack_recursive(profits, weight, capacity, currentIndex + 1)
    return max(profit1, profit2)
```

* the time complexity o(2^n) --> every item has 2 choise: select or not select
* the space complexity o(n)

### Memoization

* In the above memoization calculation problem, we have overlapping subcalculation

```
def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_recursive(dp, profits, weights, capacity, 0)

def knapsack_recursive(dp, profits, weights, capacity, currentIndex):
    if capacity <= 0 or currentIndex >= len(profits):
        return 0
    
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]
    
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex] + knapsack_recursive(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex+1)

    profit2 = knapsack_recursive(
        dp, profits, weights, capacity, currentIndex+1
    )
    
    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]
```


### Bottom-up Dynamic programming

* This is really helpful method for dynamic programming
* `dp[i][c]` will give the final result
* 


```
def solve_knapsack(profits, weights, capacity):
    n = len(profit)
    # check edge 
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0
    
    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns
    for i in range(0, n):
        dp[i][0] = 0
    
    # initialization
    for c in range(c, capacity+1):
        dp[0][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
        for c in range(1, capacity+1):
            profit1, profit2 = 0, 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i-1][c-weights[i]]
            profit2 = dp[i-1][c]
            dp[i][c] = max(profit1, profit2)
    
    return dp[n-1][capacity]

# time complexity o(N*c)
# space complxity o(N*c)
```