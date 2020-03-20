class Solution:
    def searchRange(self, nums, target):

        # two pointer solution
        left, right = 0, len(nums) - 1
        res = []
        single = - float('inf')

        while left <= right:
            if nums[left] == target and nums[right] == target:
                res.append(left)
                res.append(right)
                break
                
            elif nums[left] != target:
                left += 1
                single = left

            elif nums[right] != target:
                right -= 1

            
        if len(res) == 2:
            return res
        elif len(res) == 0:
            return [-1, -1]
        elif single:
            return [single] * 2
        
    
        