
# Maximum Number of Eaten Apples

class Solution:
    
    def eatenApples(self, apples, days):
        
        n = len(apples)
        count = 0
        heap = []
        i = 0
        while i < n or heap:
            if i < n: heap.heappush(heap, (i + days[i] -1, apples[i]))
            
            while heap and heap[0][0] < i: heapq.heappop(heap)
            
            i += 1
            if not heap: continue
            (day, apple) = heapq.heappop(heap)
            
            if apple - 1 > 0: heapq.heappush(heap, (day, apple-1))
           
            count += 1
        
        return count

# n(logn) solution here!
