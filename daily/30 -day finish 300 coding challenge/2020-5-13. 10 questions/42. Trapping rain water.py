class Solution:
    def trap(self, height):
        # find the maximum left water and right water
        # find the contribution for each slot

        # the idea is flooding all the slot
        # and look the contribution for each slot
        left = [0] * len(height)
        right = [0] * len(height)

        left[0] = height[0]
        height[-1] = height[-1]

        # buid the wall
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        for j in range(len(height)-2, -1, -1):
            right[j] = max(right[j+1], height[j])
        
        res = 0
        for i in range(len(height)):
            contri = min(left[i], right[i]) - height[i]
            if contri > 0:
                res += contri
        return res

# time complexity o(N)
# space complexity o(N)

# OPTIMIZATION THE SPACE COMPLEXITY
################## WE HAVE BETTER SOLUTION FOR THE CALCULATION ###############