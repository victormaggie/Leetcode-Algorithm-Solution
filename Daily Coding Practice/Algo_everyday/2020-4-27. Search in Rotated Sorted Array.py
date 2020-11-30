
class Solution(object):
    def search(self, nums, target):
        
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            # be aware of the >= cover only 1 number case
            elif nums[mid] >= nums[0]:
                if nums[0] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[-1]:
                # be aware of the case
                if nums[-1] >= nums[mid] and nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # time complexity o(logN)
    # space complexity o(1)