
# Next Permutation

class Solution:
    
    def nextPermutation(self, num: List[int]) -> None:
        
        i = j = len(num) - 1
        
        # descending order
        
        while i > 0 and num[i-1] >= num[i]:
            
            i -= 1
            
        if i == 0: return num.sort()
        
        k = i - 1
        
        while num[j] <= num[k]:
            
            j -= 1
        
        num[k], num[j] = num[j], num[k]
        
        l, r = k + 1, len(num) - 1
        
        while l < r:
            
            num[l], num[r] = num[r], num[l]
            l += 1
            r -= 1
        
# o(n) solution

