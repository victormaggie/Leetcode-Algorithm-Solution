class Solution:
    def reverseWords(self, s):
        if s == None:
            return 
            
        return ' '.join(s.split()[::-1])

# time complexity o(n)
# space complexity o(1)
