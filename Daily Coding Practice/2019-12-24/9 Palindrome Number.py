class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        reverse = int(str(x)[::-1])
        return reverse == x

# time complexity o(logn)
# space complexity o(1)
