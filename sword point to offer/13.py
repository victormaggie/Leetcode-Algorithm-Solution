# Hash table solution --> space complexity is not good

def duplicateInArray(nums):
    import collections
    if nums == None: return -1

    hash_table = collections.defaultdict(int)

    # detect if we have the negative number
    # for i in nums: 
    #     if i < 0: return -1

    for i in nums:
        if i < 0: return -1        # detect if we have the negative number
        hash_table[i] = hash_table[i] + 1 if i in hash_table else 0

        if hash_table[i] > 1:
            return i
    return -1
    
    # time complexity o(n)
    # space complexity o(n)


# optimization use the list swap


