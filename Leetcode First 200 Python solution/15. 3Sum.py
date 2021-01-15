
# remember the 3 sum  , brute force o(n^3)
# we need to 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # brute force solution could be o(n^3)
        nums.sort()
        
        ans = []
        for i in range(len(nums)-2):
            
            # get rid of the duplicate one
            if i and nums[i] == nums[i-1]: continue
            
            left, right = i + 1, len(nums)-1
            
            # use the two pointer solution
            target = -nums[i]
            while left < right:
                
                tot = nums[left] + nums[right]
                
                if tot > target: right -= 1
                
                elif tot < target: left += 1
                
                else: 
                    
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # move the left and right pointer
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    
                    left += 1
                    
                    while right > left and nums[right] == nums[right-1]:
                        right -= 1
                    
                    right -= 1
            
        return ans

# o(n^2) , combine two point solution and sort array here!
