class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []
        
        # edge case here
        if not nums: return []
        
        # the initial range
        rangeStart, rangeEnd = 0, math.inf
        
        # the initial maxvalue
        currentMaxNumber = -math.inf
        
        for arr in nums:
            heappush(heap, (arr[0], 0, arr))
            currentMaxNumber = max(currentMaxNumber, arr[0])
        
        # each array take one number !
        while len(heap) == len(nums):
            
            val, i, arr = heappop(heap)
            
            if currentMaxNumber - val < rangeEnd - rangeStart:
                rangeEnd = currentMaxNumber
                rangeStart = val
                
            if len(arr) > i + 1:
                heappush(heap, (arr[i+1], i + 1, arr))
                currentMaxNumber = max(currentMaxNumber, arr[i+1])
            
        return [rangeStart, rangeEnd]