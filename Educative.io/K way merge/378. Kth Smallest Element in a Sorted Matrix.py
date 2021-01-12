
# 378 Kth smallest element in a sorted matrix

class Solution:
    
    def KthSmallest(self, matrix):
        
        heap = []
        
        if not matrix: return 0
        
        if i, arr in enumerate(matrix):
            
            if arr: heapq.heappush(heap, (arr[0], i, arr))
            
        n = len(matrix)
        
        while k:
            if heap:
                (val, i, array) = heapq.heappop(heap)
            
            array.pop(0)
            
            if array: heapq.heappush(heap, (array[0], i + n, array))
            
            k -= 1
            if k == 0: return val

# o(n) solution here!
            