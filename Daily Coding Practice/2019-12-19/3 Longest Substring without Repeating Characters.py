class Solution:
    def lengthOfLongestSubstring(self, s):
        
        hash_table = {}
        pointer = 0
        maximum = 0

        for k, v in enumerate(s):
            # double check this case
            if v in hash_table and hash_table[v] > pointer:
                pointer = hash_table[v]
                hash_table[v] = k
            else:
                hash_table[v] = k
                maximum = max((k - pointer + 1), maximum)
        
        return maximum

