class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        if not a:
            return 0
        return len(a[-1])

