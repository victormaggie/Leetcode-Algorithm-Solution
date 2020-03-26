# Brute force solution

class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return nums.index(max(nums))
        
        fast = 2
        curr = 1
        slow = 0

        while fast <= len(nums):

            if fast == len(nums):
                fast_val = -float('inf')
            else:
                fast_val = nums[fast]
                slow_val = nums[slow]
                curr_val = nums[curr]
            
            if curr == 1 and slow_val > curr_val:
                return slow
            
            if fast == len(nums) -1 and fast_val > curr_val:
                return fast
            
            if curr == 1 and slow_val > curr_val:
                return slow
            
            if curr_val > slow_val and curr_val > fast_val:
                return curr
            
            curr += 1
            slow += 1
            fast += 1

# time complexity o(n)
# space complexity o(1)


class Solution:
    def findPeakElement(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1
    