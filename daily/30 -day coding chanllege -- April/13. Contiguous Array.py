class Solution:
    def findMaxLength(self, nums):
        hash_table = {}
        count = 0
        max_len = 0
        # be aware of initialization
        hash_table[0] = -1
        if i in range(0, len(nums)):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            
            if count not in hash_table:
                hash_table[count] = i 
            else:
                max_len = max(i-hash_table[count], max_len)
        
        return max_len
    
    # time complexity o(n)
    # space complexity o(n)

    