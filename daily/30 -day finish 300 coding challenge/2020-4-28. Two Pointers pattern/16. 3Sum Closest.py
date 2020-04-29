class Solution:
    def threeSumClosest(self, nums, target):
        N = len(nums)
        nums.sort()
        res = float('inf')
        for t in range(N):
            i, j = t + 1, N -1
            while i < j:
                temp = nums[i] + nums[j] + nums[t]
                if abs(target - temp) < abs(res - target):
                    res = temp
                elif target - temp == 0:
                    return target
                elif target - temp < 0:
                    j -= 1
                elif target - temp > 0:
                    i += 1
        return res

# time complexity o(N^2)
# space complexity o(N)
