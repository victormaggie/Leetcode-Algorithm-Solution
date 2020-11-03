class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # use the two pointer solution here
        nums = sorted(nums)        
        # iterate one pointer
        ans = []
        
        for i in range(len(nums)-2):
            if i and nums[i-1] == nums[i]: continue
                
            # define left and right pointer
            left = i + 1; right = len(nums)-1; target = -nums[i]
            
            if nums[i] > 0: break
            
            while left < right:
                # larger than target
                if nums[left] + nums[right] > target:
                    right -= 1
                # smaller than target
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    # update the new starting point here, avoiding duplicate answer
                    while left < right and nums[left] == nums[left+1]: left += 1
                    while left < right and nums[right] == nums[right-1]: right-=1

                    left += 1
                    right -= 1
        
        return ans

