class Solution:
    def findKthLargest(self, nums, k):
        result = []
        for num in nums:
            if len(result) < k:
                heapq.heappush(result, i)
                continue
            heappushpop(result, i)
        
        return result[0]
    
# n log k