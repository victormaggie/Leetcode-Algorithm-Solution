# use the cyclic sort 
# this can be solved in o(n)

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        # this is the index for the calculation
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    return nums

# time complexity o(n)
# space complexity o(1)


