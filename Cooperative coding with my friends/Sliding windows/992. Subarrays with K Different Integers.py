from typing import List
import collections

class Solution:
    def subarraysWithDistinct(self, A: List[int], K: int) -> int:

        # use a hashset to store the value
        hashmap = collections.default(int)

        front, end = 0, 0
        res = 0

        for front in range(len(A)):
            
            hashmap[A[front]] += 1
            if len(hashmap) == K:
                res += 1
            
            elif len(hashmap) > K:
                while len(hashmap) > K:
                    hashmap[A[end]] -= 1
                    end += 1

        return res

# time complexity o(n)
# space complexity o(n)


