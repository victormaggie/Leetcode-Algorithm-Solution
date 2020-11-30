class Solution:
    def maxLenghtBetweenEqualCharacters(self, s):

        hashmap = {}
        ans = 0
        for i in range(len(s)):
            if s[i] in hashmap:
                ans = max(i - hashmap[s[i]]-1, ans)
                continue
        
        if len(hashmap) == len(s): return -1
        return ans
    
# o(n) solution here!