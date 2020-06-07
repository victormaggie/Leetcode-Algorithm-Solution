### Longest Palindromic Subsequence

* using dynamic programming to solve palindromic subsequence

    * Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
      * `input: abdbca` and output `5` Explanation: LPS is `"abdba"`
    * Brute force solution 
        ```
        def find_LPS_length(st):
            return find_LPS_length_recursive(st, 0,  len(st)-1)
        
        def find_LPS_length_recursive(st, startIndex ,endIndex):
            if startIndex == endIndex:
                return 0
            # every sequence with one element is a palindrome of length 1
            if st[startIndex] == st[endIndex]:
                return 1
            
            # Case 1: we move together with index 
            if st[startIndex] == st[endIndex]:
                return 2 + find_LPS_length_recursive(st, start+1, end-1)
            
            # Case 2: we either move start 1 or end 1
            c1 = find_LPS_length_recursive(st, start+1, end)
            c2 = find_LPS_length_recursive(st, start, end-1)

            return max(c1, c2)
        ```
    * Top down Dynamic Programming with Memoization
      * Here we have duplicate calculation, we can use a memoization array
        ```
        def find_LPS_length(st):
            n = len(n)
            # becase the value is represented with start index and end index
            # as such, we can use the a memozaition to do the calculation
            dp = [[-1 for i in range(n)] for j in range(n)]
            return find_LPS_length_recursive(st, dp, 0, len(st)-1)
        
        def find_LPS_length_recursive(st, dp, startIndex, endIndex):
            if startIndex > endIndex: return 0
            if startIndex == endIndex: return 1

            if dp[startIndex][endIndex] == -1:
                if st[startIndex] == st[endIndex]:
                    dp[startIndex][endIndex] = 2 + find_LPS_length_recursive(st, dp, startIndex+1, endIndex-1)
                else:
                    c1 = find_LPS_length_recursive(st, dp, startIndex + 1, endIndex)
                    c2 = find_LPS_length_recursive(st, dp, startIndex, endIndex+1)
                    dp[startIndex][endIndex] = max(c1, c2)
            
            return dp[startIndex][endIndex]
        ```
    * Bottom up Dynamic programming
      * the bottom up dynamic programming is a lot easier
        ```
        def find_LPS_length(st):
            n = len(st)
            dp = [[0 for _ in range(n)] for _ in range(n)]

            for i in range(n):
                dp[i][i] = 1
            
            for startIndex in range(n-1, -1, -1):
                for endIndex in range(startIndex+1, n):
                    if st[startIndex] == st[endIndex]:
                        dp[startIndex][endIndex] = 2 + dp[startIndex+1][endIndex-1]
                    else:
                        dp[startIndex][endIndex] = max(
                            dp[startIndex+1][endIndex], dp[startIndex][endIndex - 1]
                        )
            return dp[0][n-1]
        
        ```