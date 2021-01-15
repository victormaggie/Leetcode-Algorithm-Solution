
# 523 Continuous Subarray Sum

class Solution:
    def checkSubarraySum(self, nums, k):
        
        if not nums: return False
        
        hashtable = collections.defaultdict(int)
        
        prefix = 0
        hashtable[0] = -1
        
        for i in range(len(nums)):
            
            prefix += nums[i]
            
            if k != 0: prefix %= k
            
            # here actually we are storing the smallest index
            if prefix in hashtable:
                if i - hashtable[prefix] > 1:
                    return True
            else:
                hashtable[prefix] = i
                
        return False
    
    # o(n) solution here!
    
