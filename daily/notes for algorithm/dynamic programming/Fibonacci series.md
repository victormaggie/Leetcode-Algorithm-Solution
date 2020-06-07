# Fibonacci Numbers

### Fibonacci numbers calculation

Fibonacci numbers are a series of numbers in which each number is the sum of two predicding numbers, e.g. 0, 1, 1, 2, 3, 5 ... 
Mathematical formula: f(n) = f(n-1) + f(n-2)

* Brute force
```
    def fibonacci(n):
        if n < 2: return n
        return fibonacci(n-1) + fibonacci(n-2)
    # time complexity: o(n^2)
    # space complexity: o(n)
```

* Dynamic programming with memozaition
```
    from functools import lru_cache
    @lru_cache(None)
    def fibonacci(n):
        # I do not wanna handle the index
        dp = [False for i in range(n+1)]
        def fibonacci(num, dp):
            if num < 2: return num
            if dp[num]: return dp[num]
            if dp[num] == False:
                dp[num] = fibonacci(num-1, dp) + fibonacci(num-2, dp)
            return dp[num]
        return fibonacci(n, dp) 
    # time complexity: o(n)
    # space complexity: o(n)
```

* Dynamic programming with bottom up
```
    def fibonacci(n):
        if n < 2: return n
        n1, n2 = 0, 1
        for i in range(n-1):
            # here use the pythonic syntax
            n1, n2 = n2, n1+n2
        return n2
    # time complexity: o(n)
    # space complexity: o(1)
```

### Case study
Fibonacci calculation is the fundamental for dynamic programming, it can be used for following questions:

* Stair climbing questions.
    * I. Given a stair with 'n' steps, implement a method to count how many possible ways are there to reach the top of the staircase, give that, at every step you can either take step 1, step 2 and step 3.

        * In the question, the transition formula is f(n) = f(n-1) + f(n-2) + f(n-3), we can have 3 possibility for the nth stair, it can be reached from n -1, n - 2, n -3 th stair, thus this is a typical fibonacci question.
        *  Solution: 
        ```
         def stair_climbing(n):  
            if n < 3: return n
            n1, n2, n3 = 1, 1, 2
            def fibonacci(n):
                for i in range(n-2):
                    n1, n2, n3 = n2, n3, n1+n2+n3
                return n3
            return fibonacci(n)
        # time complexity: o(n)
        # space complexity: o(n)
        ```
* Number factors
  * I. Given a number 'n', implement a method to count how many possible ways there are to express 'n' as the sum of 1, 3, or 4
    ```
    # base case
    from functools import lru_cache
    @lru_cache(None)
    def count_ways(n):
        # case 1:
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2

        return count_ways(n-1) + count(n-3) + count(n-4)

    ```

    * AKA, there's a lot of duplicate calculation for this case, as we top down to calculate the result. Then we can use memozaition to do the calculation.
    * `dp = [-1 for i in range(n+1)]` , the memoization array
  
  * Memozaition solution for top down approach.
    ```
    from functools import lru_cache
    def count_ways(n):
        dp = [-1 for i in range(n+1)]
        return recursive(dp, n)
    @lru_cache(None)
    def recursive(dp, n):
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 1
        if n == 3: return 2

        # memozaition part here
        if dp[n] != -1: return dp[n]
        if dp[n] == -1:
            # case 1:
            case1 = count_way(dp, n-1)
            # case 2:
            case2 = count_way(dp, n-3)
            # case 3:
            case3 = count_way(dp, n-4)
            dp[n] = case1 + case2 + case3
        return dp[n]
    ```
    * This solution is pretty elegant, we can also use the lru_cache funtion to hash the memory
  * Bottom up solution, this question can be calculate with following fibonacci formula:
    `fibonacci(n) = fibonacci(n-1) + fibonacci(n-3) + fibonacci(n-4) for n >= 4`
    However, this is **not continuous** fibonacci, thus we need 1 array to memorize the previous calculation results.
    ```
        def count_ways(n):
            dp = [0 for i in range(n+1)]
            dp[0] = 1
            dp[1] = 1
            dp[2] = 1
            dp[3] = 2
            for i in range(4, n+1):
                dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
            return dp[n]
    ```
* Minimum jumps to reach the end  --> Jump Game Leetcode 45 55 Question
  * Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array. If an element is 0, then we can not move through that element.
  `input = {2, 1, 1, 1, 4} output = 4  Explanation: Starting from index 0`
    * The brute force solution
    
    ```
        def count_min_jumps(jumps):
            return count_min_jumps_recursive(jumps, 0)
        def count_min_jumps_recursive(jumps, currentIndex):
            if currentIndex = len(jumps)-1: return 0

            # this cannot move 
            if jumps[currentIndex] == 0:
                return math.inf

            totalJumps = math.inf
            # find the new index range
            start, end = currentindex + 1, currentindex + jumps[currentIndex] 
            while start < n and start <= end:
                minJumps = count_min_jumps_recursive(jumps, start)
                start += 1
                if minJumps != math.inf:
                    totalJumps = min(totalJumps, minJumps + 1)
            return totalJumps
    ```

    * The memorization solution
    ```
        def count_min_jumps(jumps):
            dp = [0 for i in range(len(jumps))]
            return count_min_jumps_recursive(jumps, 0)
        
        def count_min_jumps_recursive(jumps, currentIndex):
            if currentIndex == len(jumps) -1: return 0
            if dp[currentIndex] != 0: return dp[currentIndex]

            start, end = currentIndex, currentIndex + jumps[currentIndex]
            totalJumps = math.inf
            while start < n and start <= end:
                if minJumps != math.inf:
                    minJumps = count_min_jumps_recursive(jumps, start)
                    start += 1
                    if minJumps != math.inf:
                        totalJumps = min(totalJumps, minJumps + 1)
            dp = totalJumps
            return dp[currentIndex]
            # This method has a problem that, if the value is very large, then it will ETL
    ```

    * Bottom up solution dynamic programming
    ```
        def count_min_jumps(jumps):
            dp = [math.inf for i in range(len(jumps))]
            while end <= start + jump[start] and end < n:
                dp[end] = min(dp[end], dp[start]+1)
                end += 1
            return dp[n-1] 
    ```

* Minimun jumps with fee
    * Given a staircase with 'n' steps and an array of 'n' numbers representing fee that you have to pay if you take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase. At every step, you have an option take either 1 step, 2 step or 3 steps.
        ```
        Numbers of stairs (n) : 6
        Fee: {1, 2, 5, 2, 1, 2}
        Output: 3
        Explanation: starting from index '0', we can reach the top through: 0 - > 3 -> top
        ```

        * This is the traditional fobonacci calculation, `min(val) = fee(i+1) * fibonacci(i) + fee(i+1) * fibonacci(i+1) + fee(i+2)*fibonacci(i+2)`
        * Bottom up solution
        ```
        def find_min_fee(fee):
            dp = [0 for i in range(len(fee))]
            dp[0] = fee[0] * 1
            dp[1] = fee[0] * 1
            dp[2] = fee[0]
            for i in range(2, n+1):
                one_step = dp[i-1] + fee[i-1]
                two_step = dp[i-2] + fee[i-2]
                three_step = dp[i-3] + fee[i-3]
                dp[i] = min(one_step, two_step, three_step)
            return dp[n]
        ```
    * House thief
      * 
