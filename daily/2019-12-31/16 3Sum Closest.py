class Solution(object):
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums.sort()
        res = float('inf')
        for t in range(N):
            i, j = t+1, N-1
            while i < j:
                temp = nums[i] + nums[j] + nums[t]
                if abs(temp - target) < abs(res - target):
                    res = temp
                if temp > target:
                    j -= 1
                elif temp < target:
                    i += 1
                else:
                    return target
        return temp

# time complexity o(n^2)
# space complexity o(1)

