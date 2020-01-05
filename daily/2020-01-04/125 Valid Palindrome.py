class Solution:
    
    def isPalindrome(self, s):
        import re
        word = ''.join(re.findall(r'\w+', s.lower()))

        return word[::-1] == word

# we can also use two pointer
