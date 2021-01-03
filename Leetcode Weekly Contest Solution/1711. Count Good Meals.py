
# 1711 Count Good Meal

class Solution:
    def countPairs(self, a):
        
        
        hashmap = collections.defaultdict(int)
        
        ans = 0
        mod = 10 ** 9 + 7
        for num in a:
            curr = 1
            for i in range(22):
                t = (1 << i) - num
                if t in hashmap:
                    ans = (ans + hashmap[4]) % mod
            hashmap[num] += 1
        
        return ans

# time complexity o(n * log22)
