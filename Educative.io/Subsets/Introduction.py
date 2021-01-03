
# subset question --> 2^N time complexity 

# A huge number of coding interview proble

# ---> Permutation 
# ---> Combination


# Question 1:

"""
    Given a set with distinct elements, find all of its distinct subsets
    Input: [1, 3]
    Output: [], [1], [3], [1,3]
"""


def find_subsets(nums):
    subsets = []
    
    def dfs(nums, idx, temp):

        for i in range(idx, len(nums)):
            temp.append(nums[i])
            # here every single value needs to be pushed in
            subsets.append(temp[:])
            dfs(nums, i+1, temp)
            temp.pop()
    
    dfs(nums, 0, [])
    return subsets
    

def find_subsets(nums):
    subsets = []
    
    subsets.append([])
    
    for num in nums:
        
        max_len = len(subsets)
        # here we can see each element will double the element (2^N)
        for i in range(max_len):
            # copy the string, its complexity o(N)
            # has to make a copy and add all
            temp = list(subsets[i])
            temp.append(num)
            subsets.append(temp)
    
    return subsets


# since each element will double the results to all the existing subsets, 
# 2 * 2 * 2 * ... = 2 ^ N

# Time complexity and space complexity o(N * 2^N)

