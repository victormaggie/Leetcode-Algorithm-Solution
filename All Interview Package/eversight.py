"""
Goal: Find the number of pairs of elements in the array the sum of which is divisible by K
Inputs: 
    a: array of positive integers
    K: the divider
Outputs:
    C: number of pairs of elements whose sum is divisible by K
Example:
    a = [1, 4, 5, 3]
    K = 3
    C = 2        # ({1, 5}, {4, 5})
"""


# for i in range(len(a)):
#     for j in range(i +1, len(a)):
#         o(n2)

# left: 1
# right : 3 
    
#     o(nlogn)

from itertools import permutations

def func(a, C, K):
    if not a: return []
    a = set(a)
    
    arr = permutations(a, C)
    res = []
    for i in arr:
        
        if i[::-1] not in res and sum(i) % K == 0:
            res.append(i)
            
    return res
    

a = [1, 4, 5, 3]
K = 3
C = 2        # ({1, 5}, {4, 5})
print(func(a, C, K))