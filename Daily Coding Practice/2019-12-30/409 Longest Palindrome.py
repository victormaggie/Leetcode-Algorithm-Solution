class Solution(object):
    def longestPalindrome(self, s):
        count = collections.Counter(s)
        res = 0
        prime = 0
        
        for i in count:
            if count[i] % 2 == 1:
                res += count[i] - 1
                prime = 1
            else:
                res += count[i]
        return res + prime
