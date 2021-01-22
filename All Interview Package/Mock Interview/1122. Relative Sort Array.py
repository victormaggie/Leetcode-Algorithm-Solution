
# 1122 Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        hashmap = collections.defaultdict(int)
        
        ans = []
        for num in arr1:
            hashmap[num] += 1
        
        for num in arr2:
            
            ans += [num] * hashmap[num]
            del hashmap[num]   
        
        hashmap = sorted(list(hashmap.items()))
        
        for num, cnt in hashmap:
            
            ans += [num] * cnt
        
        return ans