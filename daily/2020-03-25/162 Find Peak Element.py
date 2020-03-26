# Brute force solution

class Solution:
    def findPeakElement(self, nums):

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
        # climbing algorithms
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return len(nums)-1
    
    # o(n)
    # o(1)

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) -  1

        # here cannot == , not search
        while left < right:
            mid = (left + right) //2 
            # going downwards
            if nums[mid] > nums[mid+1]:
                right = mid
            # going upwards
            else:
                left = mid + 1
        return left

# o(log2n)
# o(1)

# Divide and Conquer solution for the algorithms

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) -1
        self.binary_search(nums, left, right)

    def binary_search(self, nums, left, right):

        if (left == right):
            return left
        
        mid = (left + right) // 2
        if (nums[mid] > nums[mid+1]):
            return self.binary_search(nums, left, mid)
        
        return self.binary_search(nums, mid+1, right)

