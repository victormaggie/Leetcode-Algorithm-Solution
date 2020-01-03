class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        # define hash_map
        s_map_t = {}
        t_map_s = {}

        for char_s, char_t in zip(s, t):
            if char_s in s_map_t:
                if s_map_t[char_s] != char_t:
                    return False
            if char_t in t_map_s:
                if t_map_s[char_t] != char_s:
                    return False
            s_map_t[char_s] = char_t
            t_map_s[char_t] = char_s
        return True

# time complexity o(n)
# space complexity o(n)

