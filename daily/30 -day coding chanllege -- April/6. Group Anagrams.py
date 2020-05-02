# brute force solution

class Solution:
    def groupAnagrams(self, strs):
        hash_table = collections.defaultdict(list)
        for i in strs:
            Flag, key, i = self.check(hash_table, i)
            if not hash_table or not Flag:
                hash_table[i] = [i]
            else:
                hash_table[key].append(i)
        return [i for i in hash_table.values()]
    
    def check_in(self, hash_table, i):
        for key in hash_table:
            if key == i:
                return (True, key, i)
            if key != i:
                if sorted(key) == sorted(i):
                    return (True, key, i)
        
        return (False, None, i)


# cannot pass the test case time limit
# o(n ^ 2)
# space complexity o(n+m)


class Solution:
    def groupAnagrams(self, strs):
        hash_table = collections.defaultdict(dict)
        for i in strs:
            hash_table[tuple(sorted(i))] += [i]
        return list(hash_table.values())