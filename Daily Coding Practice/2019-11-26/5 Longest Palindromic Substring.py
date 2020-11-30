class Solution:
    def longestPalindrome(self, s):
        ans = ''
        
        for i in range(len(s)):
            len1 = len(self.isPalin(s, i, i))

            if len1 > len(ans):
                ans = self.isPalin(s, i, i)

            len2 = len(self.isPalin(s, i, i+1))

            if len2 > len(ans):
                ans = self.isPalin(s, i, i+1)

        return ans

    def isPalin(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
