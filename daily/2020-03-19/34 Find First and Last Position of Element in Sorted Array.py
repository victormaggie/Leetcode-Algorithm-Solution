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
        
    
    # time complexity o(n)
    # space complexity o(1)

    def searchRange2(self, nums, target):

        # binary search algorithm
        res = None
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left, right = mid, mid
                while left >= 0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                res = [left + 1, right - 1]
                break
            elif nums[mid] > target:
                right = mid - 1   
            elif nums[mid] < target:
                left = mid + 1
        
        if not res:
            return [-1, -1]
        return res
    
    # time complexity o(n + logn)
    # space complexity o(n)

    def searchRange3(self, nums, target):

        left_idx = self.extreme_insertation_index(nums, target, True)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]
        
        return [left_idx, self.extreme_insertation_index(nums, target, False) -1]

    def extreme_insertation_index(self, nums, target, boolean):
        left, right = 0, 1

        while left <= right:
            mid = (left+ right) //  2
            # find the left most value for the algorithm
            # find the right most value for the algorithm
            if nums[mid] > target or (boolean and target == nums[mid]):
                right = mid -1
            else:
                left = mid + 1

        return left

    # time complexity o(logn)
    # space complexity o(1)

    
