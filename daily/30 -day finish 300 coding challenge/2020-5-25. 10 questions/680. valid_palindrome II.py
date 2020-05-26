class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                temp1 = s[:left] + s[left+1:]
                temp2 = s[:right] + s[right+1:]
                return temp1 == temp1[::-1] or temp2 == temp2[::-1]
        return True


# # look at the greedy solution