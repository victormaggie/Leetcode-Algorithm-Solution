class Solution:
    def checkPalindromeFormation(self, S, T):

        def palindrome(A, i, j):
            if i >= j: return True

            for k in range(j - i + 1):
                if A[i+k] != A[j-k]: return False
            
            return True
        
        N = len(S)
        i = 0
        j = N - 1

        while i < j and S[i] == T[j]:
            i += 1
            j -= 1
        
        if palindrome(S, i, j) or palindrome(T, i, j):
            return True
        
        i = 0
        j = N - 1
        while i < j and S[j] == T[i]
            i += 1
            j -= 1
        
        if palindrome(S, i, j) or palindrome(T, i, j):
            return True
        
        return False

# time complexity o(n)
# space compelxity o(1)
