# 4 sum II
class Solution:
    def fourSumCount(self, A, B, C, D):
        
        hashtable = collections.defaultdict(int)
        
        for a in A:
            for b in B:
                hashtable[a + b] +=1
        
        ans = 0
        
        for c in C:
            for d in D:
                ans += hashtable[-c - d]
        
        return ans

# o(n^2) solution here