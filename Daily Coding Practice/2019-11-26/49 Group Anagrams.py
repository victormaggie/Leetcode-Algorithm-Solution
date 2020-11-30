import collections
class Solution:
    def groupAnagrams(self, strs):

        # use hash_table to store the same key
        # use the dictionary values
        hash_table = collections.defaultdict(list)
        for i in strs:
            stri = tuple(sorted(i))
            hash_table[stri] += [i]

        return list(hash_table.values())