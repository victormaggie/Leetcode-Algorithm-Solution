class solution(object):
    
    def findTheDifference(self, s, t):
        import collections
        hash_table = collections.defaultdict(int)
        for i in t:
            hash_table[i] += 1 if i in t else 0
        
        for j in s:
            hash_table[j] -= 1 if j in hash_table else 1
            if hash_table[j] == 0:
                del hash_table[j]
        
        return hash_table.keys()[0]

# time complexity o(n+m)
# space complexity o(n)

    def findTheDifference1(self, s, t):
        # bitwise solution
        return chr(sum(ord(t)) - sum(ord(s)))

