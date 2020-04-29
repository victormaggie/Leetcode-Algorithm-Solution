class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = {}
        cnt = 0
        for i in s:
            # not in the array
            if hash_table.get(i, 0):
                hash_table[i] = cnt
            else:
                # in the array
                del hash_table[i]
            cnt += 1


        return next(iter(hash_table.values()))
        
        