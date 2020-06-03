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
    
