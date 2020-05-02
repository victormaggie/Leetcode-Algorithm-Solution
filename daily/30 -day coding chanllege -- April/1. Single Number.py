# Given a non-empty array of integers, every element appears twice except for one

Class solution:
    def singleNumber(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a

# time complexity o(n)
# space complexity o(1)

Class Solution:
    def singleNumber(self, nums):
        return sum(set(nums)) * 2 - sum(nums)

# time complexity o(n + n)  set and sum all o(n)
# space complexity o(n)  set needs space for the element

Class Solution:
from collections import defaultdict
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

# time complexity o(1.n) = o(n) 
# space complexity o(n)

class solution:
    def singleNumber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list[-1]
    
# time complexity o(n^2)
# space complexity o(n)

