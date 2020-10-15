class Solution:
    def longestPalindrome(self, s):

        # longest palindrome substring

        ans = ''
        for i in range(len(s)):
            ans1 = self.ispalindrome(s, i, i+1)
            if len(ans1) > len(ans):
                ans = ans1
            
            ans2 = self.ispalindrome(s, i, i)
            if len(ans2) > len(ans):
                ans = ans2
            
            if len(ans) == len(s): return ans

        return ans
    
    def ispalindrome(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left+1: right]
    
    # time complexity o(n^2)
    # space o(1)



# brute force solution

def find_LPS_length(st):
    return find_LPS_length_recursive(st, 0, len(st)-1)

def find_LPS_length_recursive(st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    
    if startIndex == endIndex:
        return 1
    
    if st[startIndex] == st[endIndex]:
        remainingLength = endIndex - startIndex - 1
        if remainingLength == find_LPS_length_recursive(st, startIndex+1, endIndex-1):
            return remainingLength + 2

    c1 = find_LPS_length_recursive(st, startIndex + 1, endIndex)
    c2 = find_LPS_length_recursive(st, startIndex, endIndex - 1)
    return max(c1, c2)

