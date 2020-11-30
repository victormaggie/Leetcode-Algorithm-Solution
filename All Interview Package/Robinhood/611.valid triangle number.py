class Solution:
    def triangleNumber(self, nums):

        # use the two pointer here

        count = 0
        nums = sorted(nums)
        for k in range(len(nums)-1, 1, -1):
            left = 0
            right = k-1
            while left < right:
                if nums[k] < nums[left] + nums[right]:
                    count += right - left
                    right -=  1
                
                else:
                    left += 1
        
        return count

# time complexity o(n^2)
# space complexity (o(1))

