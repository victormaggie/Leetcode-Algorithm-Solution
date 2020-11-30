class solution(object):
    def threeSum(self, nums):

        N = len(nums)
        nums.sort()
        res = []
        for t in range(N - 2):
            # delete the duplicated one
            if t > 0 and nums[t] == nums[t - 1]:
                    continue
            i, j = t + 1, N - 1
            while i < j:
                _sum = nums[t] + nums[i] + nums[j]
                if _sum == 0:
                    res.append([nums[t], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # delete the duplicated one
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    # delete the duplicated one
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif _sum < 0:
                    i += 1
                else:
                    j -= 1
        return res

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # nlogn sort
        nums = sorted(nums)
        
        res = []
        i = 0
        n = len(nums)
        while i < n -2:
            left = i + 1
            right = n - 1

            while left < right :

                Sum = nums[i] + nums[left] + nums[right]
                if Sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left = self.move_left(nums, left+1)
                    right = self.move_right(nums, right-1)

                elif Sum > 0:
                    right = self.move_right(nums, right-1)

                elif Sum < 0:
                    left = self.move_left(nums, left+1)    
            
            i = self.move_left(nums, i+1)

        return res
    
    
    def move_left(self, nums, left):
        while (left == 0 or (left < len(nums)-1 and nums[left] == nums[left-1])):
            left += 1
        return left
    
    def move_right(self, nums, right):
        while (right == len(nums)-1 or (right > 0 and nums[right] == nums[right+1])):
            right -= 1
        return right