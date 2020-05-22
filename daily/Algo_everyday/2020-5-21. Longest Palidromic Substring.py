class Solution:
    def longestPalindrome(self, s):
        ans = ''

        for i in range(len(s)):
            # the odd number
            temp1 = self.isPalindrome(s, i, i)
            if len(ans) < len(temp1):
                ans = temp1
            
            # the even number
            temp2 = self.isPalindrome(s, i, i+1)
            if len(temp2) > len(ans):
                ans = temp2
            
            # Prune the recursion
            if len(ans) == len(s):
                return ans

        return ans
    
    def isPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]

# time complexity o(n^2)
# space complexity o(1)

# recursion solution need to think about the prune 
# without prune 1600 ms
# prune 560 ms  ---> nice!