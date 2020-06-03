class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        # Brute force solution o(n^2)
        area = 0 
        for i in range(len(heights)):
            min_val = float('inf')
            for j in range(i, len(heights)):
                min_val = min(min_val, heights[j])
                area = max(area, min_val * (j-i+1))
        return area

    # divide and conquer approach o(nlog n)
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if not heigths: return 0
        def divide_conquer(heights, start, end):
            if start > end: return 0
            minindex = start
            for i in range(start, end+1):
                if heights[minindex] > heights[i]:
                    minindex = i
            return max(heights[minindex]*(end-start+1), max(divide_conquer(heights, start, minindex-1), divide_conquer(heights, minindex+1,end)))
        return divide_conquer(heights, 0, len(heights)-1)
    
    # time complexity o(nlogn)

    # Stack solution

    def largestRectangleArea3(self, heights: List[int]) -> int:
        if not heights: return 0
        stack = [-1]
        area = 0

        for i in range(0, len(heights)):
            while stack[-1] != -1 and stack[-1] > heights[i]:
                area = max(area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        
        while stack[-1] != -1:
            area = max(area, heights[stack.pop()] * (len(heights) - stack[-1] -1) )
        
        return area
# time complexity o(n)
# space complexity o(n)


