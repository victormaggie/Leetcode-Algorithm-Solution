class Solution(object):
    def reverseVowels(self, s):
        # vowels = ['a','A', 'e','E','i','I','o','O','u','U']
        vowels = 'aAeEiIoOuU'

        if not s:
            return ''
        
        s = list(s)
        left, right = 0, len(s)-1
        while left <= right:
            if s[left] not in vowels:
                left += 1
            elif s[right] not in vowels:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right += 1
        return ''.join(s)

# time complexity o(n)
# space complexity o(N)

