### Longest Palindromic Subsequence

* using dynamic programming to solve palindromic subsequence

    * Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
      * `input: abdbca` and output `5` Explanation: LPS is `"abdba"`
    * Brute force solution 
        ```
        def find_LPS_length(st):
            return find_LPS_length_recursive(st, 0,  len(st)-1)
        
        def find_LPS_length_recursive(st, startIndex ,endIndex):
            if startIndex > endIndex:
                return 0
            # when it is like 'aba'  --> for b, the startIndex == endIndex then return 1
            if startIndex == endIndex:
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
            # be aware of the dp solution -> two cases
            if dp[startIndex][endIndex] == -1:
                if st[startIndex] == st[endIndex]:
                    dp[startIndex][endIndex] = 2 + find_LPS_length_recursive(st, dp, startIndex+1, endIndex-1)
                else:
                    c1 = find_LPS_length_recursive(st, dp, startIndex + 1, endIndex)
                    c2 = find_LPS_length_recursive(st, dp, startIndex, endIndex-1)
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
                # be aware of that here, we move from the diagnal
                    if st[startIndex] == st[endIndex]:
                        dp[startIndex][endIndex] = 2 + dp[startIndex+1][endIndex-1]
                    else:
                        dp[startIndex][endIndex] = max(
                            dp[startIndex+1][endIndex], dp[startIndex][endIndex-1]
                        )
            return dp[0][n-1]
        
        ```
        time complexity: o(n^2)
        space complexity: o(n^2 + n)

## Longest Palindromic Substring

* This question is pretty much like the question of  subsequence
  * `abdbca`
  * `output: 3` -> `bdb`
  
  * Brute force solution
    ```
    def find_LPS_length(st):
        return find_LPS_length_recursive(st, 0, len(st)-1)
    
    def find_LPS_length_recursive(st, startIndex, endIndex):
        # stop condition
        if startIndex > endIndex:
            return 0
        if startIndex == endIndex: return 1

        if st[startIndex] == st[endIndex]:
            remainingLenght = startIndex - endIndex -1
        
            # check if the remaining length is also a Palindrome
            if remainingLength == find_LPS_length_recursive(st, startIndex+1, endIndex-1):
                return remainingLength + 2
        
        # case 2: skip one character either from the begining or the end
        c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
        c2 = find_LPS_length_recursive(st, startIndex, endIndex -1)
        return max(c1, c2)
    ```

  * Top down solution with memozaition
    ```
    def find_LPS_length(st):
        dp = [[-1 for i in range(len(st))] for j in range(st)]
        return find_LPS_length_recursive(st, 0, len(st)-1)
    
    def find_LPS_length_recursive(st, startIndex, endIndex):
        if startIndex > endIndex: return 0
        if startIndex == endIndex: return 1
        if dp[startIndex][endIndex] != -1: return dp[startIndex][endIndex]


        if dp[startIndex][endIndex] == -1:
            # case 1: left and right char are the same
            if st[startIndex] == st[endIndex]:
                remainingLength = endIndex - startIndex - 1
                if remainingLength == find_LPS_length_recursive(st, startIndex+1, endIndex-1):
                    return remainingLength + 2
            # case 2: we move the left
            c1 = find_LPS_length_recursive(st, startIndex, endIndex-1)
            # case 3: we move the right
            c2 = find_LPS_length_recursive(st, startIndex+1, endIndex)
            dp[startIndex][endIndex] = remainingLength
        return dp[startIndex][endIndex]
        # time complexity o(3^n)

    ```

  * Bottom up solution
    * the bottom up solution is really the same as the previous one.
    ```
    def find_LPS_length(st):
        n = len(st)
        dp = [[0 for i in range(n)] for j in range(n)]
        # initialization 
        for i in range(n):
            dp[i][i] == 1
        
        maxLength = 1
        for startIndex in range(n-1, -1, -1):
            for endIndex in range(i+1, n):
                if st[startIndex] == st[endIndex]:
                    # if it is two character string
                    # if the subsequence is a palindromn as well
                    if endIndex - startIndex == 1 or dp[startIndex + 1][endIdnex -1]:
                        dp[startIndex][endIndex] = True
                        maxLength = max(maxLength, endIndex - startIndex + 1)
        return maxLength
        # time complexity o(n^2)
    ```

* Count of Palindromic substring
  * Given a string, find the total number of palindromic substring in it.
    * Bottom up solution
    ```
    def count_PS(st):
        n = len(st)
        # dp[i][j] will be true if the string from index 'i' to 'j' is palindrome
        dp = [[False for _ in range(n)] for _ in range(n)]

        for startIndex in range(n-1, -1, -1):
            for endIndex in range(startIndex+1, n):
                if st[startIndex] == st[endIndex]:
                    if startIndex - endIndex == 1 or dp[startIndex + 1][endIndex-1]:
                        dp[startIndex][endIndex] = True
                        count += 1
        return count
        # time complexity: o(n^2)
    ```

* Minimum deletions in a string to make it a Palindrome
  if we can figure out the maximum length of Palindrome, then use the origin length to substract it.
```
    def find_LPS_length(st):
        n = len(st)
        dp = [[0 for i in range(n)] for j in range(n)]
        # initialization the matrix
        for i in range(n):
            dp[i][i] = 1
        
        for startIndex in range(n-1, -1, -1):
            for endIndex in range(startIndex+1, n):
                if st[startIndex] = st[endIndex]:
                    dp[startIndex][endIndex] = 2+ dp[startIndex+1][endIndex-1]
                else:
                    dp[startIndex][endIndex] = max(
                        dp[startIndex+1][endIndex], dp[startIndex][endIndex-1]
                    )
        return n - dp[0][n-1]

```

  * Palindrome partition
    * Given a string, we want to cut it into pieces such that each piece is a palindrome,
      * `abcbca`
      * `3`
      * palindrome pieces are `a`, `bdb`, `c`, `a`

    * Brute force solution
    ```
    def find_MPP_cuts(st):
        n = len(st)
        return find_MPP_cuts(st, 0, n-1)
    
    def find_MPP_cuts_recursive(st, startIndex, endIndex):
        # stop condition or if it is palindrome, we do not need to cut
        if startIndex > endIndex or is_palindrome(st, startIndex, endIndex):
            return 0

        # at max, we need to cut the string into length - 1 pieces
        minimum_cuts = endIndex - startIndex
        # if all is palindrome, then startIndex = endIndex, minimum_cuts = 0
        for i in range(startIndex, endIndex):
            if is_palindrome(startIndex, i):
            # cut once at i index
                minimum_cuts = min(
                    minimum_cuts, 1 + find_MPP_cuts_recursive(st, i+1, endIndex)
                )
        return minimum_cuts
    
    def is_palindrome(st, x, y):
        while (x < y):
            if st[x] != st[y]:
                return False
            x += 1
            y -= 1
        return True

        # time complexity o(2^n)
    ```

    * Since here we have two helper function, `find_MPP_cuts` and `is_palindrome` , we can use a two diemension array to store the value and do memozaition.
    ```
    def find_MPP_cuts(st):
        n = len(st)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp_ispalindrome = [[-1 for _ in range(n)] for _ in range(n)]
        return find_MPP_cuts(st, dp, dp_ispalindrome, 0, n-1)
    
    def find_MPP_cuts(st, dp, dp_ispalindrome, startIndex, endIndex):
        if startIndex > endIndex or dp_ispalindrome[startIndex][endIndex]: return 0
        if dp[startIndex][endIndex] != -1: return dp[startIndex][endIndex]
        
        minimum_cut = endIndex - startIndex
        for i in range(startIndex, endIndex):
            for j in range(startIndex, i+1):
                if dp_ispalindrome[i][j]:
                    dp[i][j] = min(
                        minimum_cut, 1 + find_MPP_cuts(st, dp, dp_ispalindrome, i+1, endIndex)
                    )
        return dp[startIndex][endIndex]
    
    def is_palindrome(dp_ispalindrome, st, x, y):
        if dp_ispalindrome[x][y] == -1:
            dp_ispalindrome[x][y] = 1
            i, j = x, y
            while i < j:
                if st[i] != st[j]:
                    dp_ispalindrome[x][y] = 0
                    break
                i += 1
                j -= 1

                # use memozaition to find if the remaining string is a palindrome
                if i < j and dp_ispalindrom[i][j] != -1:
                    dp_ispalindrome[x][y] = dp_ispalindrome[i][j]
                    break
        return True if dp_ispalindrome[x][y] == 1 else False
    ```

    * # Bottom up solution do it later!! This is really difficult question!