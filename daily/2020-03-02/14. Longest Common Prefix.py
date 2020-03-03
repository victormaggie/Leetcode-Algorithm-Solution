class Solution:
    def longestCommonPrefix(self, strs):
        def find(it):
            try:
                x = next(it)
                return "" if len(set(x)) > 1 else x[0] + find(it)
            except:
                return ""
        
        return find(zip(*strs))
        