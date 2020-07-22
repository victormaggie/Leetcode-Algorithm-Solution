class Solution:
    def trap(self, height: List[int]) -> int:

        # monotonic sort solution ---> descreasing stack!!

        stack = []
        res = 0

        for currentIndex in range(len(height)):
            while stack and height[stack[-1]] < height[currentIndex]:
                index = stack.pop()
                if not stack: break
                distance = currentIndex - stack[-1] -1
                value = min(height[currentIndex], height[stack[-1]]) - height[index]
                res += distance * value 
            stack.append(currentIndex)
        
        return res
    
# monotonic sort time complexity o(n)
# space complexity o(n)


# we can also use dynamic programming
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        n = len(height)
        left_most = [0] * n
        right_most = [0] * n

        # initialization the boundary
        left_most[0] = height[0]
        right_most[-1] = height[-1]

        for i in range(1, n):
            left_most[i] = max(left_most[i-1], height[i])

        for i in range(n-2, -1, -1):
            right_most[i] = max(right_most[i-1], height[i])
        
        res = 0
        for i in range(n):
            val = min(left_most[i], right_most[i]) - height[i]
            if val >= 0:
                res += val
        
        return res

# time complexity o(n)
# space complexity o(n)

