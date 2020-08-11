class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        i = j = len(nums) - 1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        # descending order
        if i == 0:
            nums.reverse()
            return
        
        # find the ascending position
        k = i - 1

        # find the smallest bigger value from behind to replace it
        while nums[j] <= nums[k]:
            j -= 1
        
        # replace
        nums[k], nums[j] = nums[j], nums[k]

        # change the behand to acending order

        l, r = j, len(nums)-1
        
        # swap
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1
            r -= 1

# time complexity o(n)
# space complexity o(1)