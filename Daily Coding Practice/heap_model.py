class solution(object):
    def heap(self, nums, target):

        import heapq
        heapq.heapify(nums)
        heapq.nsmallest(K, heap)
        return 

class Solution(object):
    def kClosest(self, points, K):
        import heapq
        if not points:
            return
        heap = []
        for i in points:
            heapq.heappush(heap, (i[0]**2 + i[1]**2, i))
        
        return [i[1] for i in heapq.nsmallest(K, heap)]
    
  
