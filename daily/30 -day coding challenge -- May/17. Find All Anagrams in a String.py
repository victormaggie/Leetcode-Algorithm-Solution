class Solution:
    def findAnagrams(self, s, p):
        # sliding window and hash method
        ns, np = len(s), len(p)
        if ns < np or not s: return []
        p_count = collections.Counter(p)
        s_count = collections.defaultdict(int)

        res = []
        for i in range(ns):
            # add the node
            s_count[s[i]] += 1
            # pop out >= np value  
            # be aware i = 0, 1, 2, 3 ... 
            if i >= np:
                if s_count[s[i-np]] == 1:
                    del s_count[s[i-np]]
                else: s_count[s[i-np]] -= 1
            if s_count == p_count:
                res.append(i - np + 1)
        return res

# time complexity o(n+p)  --> hash and iteration
# space complexity o(n)
