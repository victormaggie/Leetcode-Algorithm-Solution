# 2020-4-17

# brute force solution o(n^2)
# two pointer solution  o(n)
class solution:
    def maxArea(self, height):
        left, right = 0, len(height)-1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[left] < height[right]:
                left += 1
            elif height[right] == height[left]:
                left += 1
                right -= 1
            else:
                right -= 1
        
        return area

# time complexity o(n)
# space complexity o(1)

# be aware of the two point!

class solution:
    def maxArea(self, height):
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                area = max(area, (j - i) * min(height[i], height[j]) )
        
        return area
# time complexity o(n)
# space complexity o(1)
