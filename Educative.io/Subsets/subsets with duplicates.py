
# subsets with Duplicates (easy)

"""

Given a set of numbers that might contain duplicates, find all of its distinct subsets

Input: [1, 3, 3]
Output: [], [1], [3], [1, 3], [1, 3, 3]
"""


def find_subsets(nums):
    
    subsets = []
    subsets.append([])
    
    def dfs(nums, idx, temp):
    
        for i in range(idx, len(nums)):
            
            if i > idx and nums[i] == nums[i-1]: continue
            temp.append(nums[i])
            subsets.append(temp[:])
            dfs(nums, i+1, temp)
            temp.pop()
    
    dfs(nums, 0, [])
    return subsets
    

# use the iterate solution for this one

def find_subsets(nums):
    subsets = []
    subsets.append([])
    
    # in order to get rid of the duplicates
    # we need to sort the array
    nums.sort()
    
    start, end = 0, 0
    
    for i in range(len(nums)):
        start = 0
        
        # This piece of code is for adding to the last piece 
        # Get rid of the duplicate one
        if i > 0 and nums[i] == nums[i-1]:
            start = end + 1
        
        end = len(subsets) - 1
        
        for j in range(start, end+1):
            temp = list(subsets[j])
            temp.append(nums[i])
            subsets.append(temp)
    
    return subsets

# time complexity o(N * 2^N)
# time complexity o(N * 2^N)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    