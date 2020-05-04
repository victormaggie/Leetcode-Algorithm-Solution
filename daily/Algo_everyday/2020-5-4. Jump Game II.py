class Solution:
    def jump(self, nums):
        n = len(nums)
        posloc = n -1 
        for i in reversed(range(n)):
            if nums[i] + i >= posloc:
                posloc = i
        return posloc == 0

# time complexity o(N)
# space complexity o(1)



class Solution:
    def jump(self, nums):
        n = len(nums)
        if n < 2: return 0

        max_pos = nums[00]
        max_steps = nums[0]

        jump = 1
        for i in range(1, n):
            if max_Steps < i:
                jump += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i]+i)
        return jump

