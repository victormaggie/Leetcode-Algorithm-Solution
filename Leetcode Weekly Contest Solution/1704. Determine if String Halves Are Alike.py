
# 1710 Maximum Units on a Truck


class Solution:
    def halvesAreAlike(self, s):
        
        hashmap = collections.defaultdict(int)
        
        n = len(s)
        half = n // 2 - 1
        
        hashset = set(['a', 'e', 'i', 'o', 'u'])
        
        for i in range(n):
            if s[i].lower() not in hashset: continue
            
            if i <= half: hashmap[s[i]] += 1
            
            if i > half: hashmap[s[i]] -= 1
            
        return sum(hashmap.values()) == 0
    
# hashmap o(n) solution
