class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        max_len = -float('inf')
        ed_window = 0
        hashset = {}
        for st_window in range(len(s)):
            if s[st_window] not in hashset: hashset[s[st_window]] = 1
            else: hashset[s[st_window]] += 1

            while len(hashset) > k:
                hashset[s[ed_window]] -= 1
                if hashset[s[ed_window]] == 0: del hashset[s[ed_window]]
                ed_window += 1
            max_len = max(max_len, ed_window - st_window + 1)
        
        # check 
        if max_len == -float('inf'): return 0
        return max_len

# time complexity o(N)
# space complexity o(k)



