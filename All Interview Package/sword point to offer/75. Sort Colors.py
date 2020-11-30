class Solution:
    def sortColors(self, nums):

        # nlog(n) algorithm

        # two pass 
        
        # one pass

        i = j = 0
        k = len(nums)-1

        while j <= k:

            if nums[j] = 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            
            elif nums[j] = 1:
                j == 1
            
            else:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
        