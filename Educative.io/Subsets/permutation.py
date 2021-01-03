
# Permutations (medium)

# Given a set of distinct numbers, find all of its permutations

# Permutation is defined as the re-arranging of the elements of the set.

# Permutation time complexity o(n!) factorial!

def find_permutations(nums):
    
    res = []
    temp = []
    
    def rec(nums, temp, res):
        if len(temp) == len(nums):
            ans.append(temp[:])
            return
        
        for i in range(len(nums)):
            if nums[i] in temp: continue
            temp.append(nums[i])
            rec(nums, temp, ans)
            temp.pop()
            
    rec(nums, temp, ans)
    return ans
    
# the factorial solution

    def generate_permutations_recursion(nums, index, currentPermuation, result):
        
        if index = len(nums):
            result.append(currentPermuation)
        
        for i in range(len(currentPermuation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            generate_permutations_recursion(
                nums, index+1, newPermutation, result)
        