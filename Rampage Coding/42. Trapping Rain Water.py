class Solution:
    def trap(self, height: List[int]) -> int;
        # edge case

        if not height: return 0

        # dynamic programming
        trap_left = [0 for i in range(n)]
        trap_right = [0 for i in range(n)]

        # initialize the first one
        trap_left[0] = height[0]
        trap_right[-1] = height[-1]

        # calculate the left most and right water
        for i in range(1, n):
            trap_left[i] = max(height[i], trap_left[i-1])
        
        for i in range(n-2, -1, -1):
            trap_right[i] = max(height[i+1], trap_right[i])

        # calculate the result
        res = 0
        for i in range(n):
            res += max(min(trap_left[i], trap_right[i]) - height[i], 0)
        
        return res

# time complexity o(n)
# space complexity o(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        stack = []
        res = 0
        for i in range(len(height)):
            if not stack:
                stack.append(i)
            while stack and height[i] > height[stack[-1]]:
                res += (stack[0] - height[stack[-1]])
                stack.pop()
                
            stack.append(i)
            
        return res