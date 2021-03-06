class Solution(object):
    def reverseString(self, s):
        s.reverse()
    
    def reverseString1(self, s):
        # two pointer solutions
        left, right = 0, len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
