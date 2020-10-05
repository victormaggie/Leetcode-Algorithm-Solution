class Solution:
    def getSkyline(self, buildings):

        events = [(L, -H, R) for L, R, H in buildings]
        
        events += [(R, 0, 0) for L, R, H in buildings]
        
        events.sort()
        
        heap = [(0, float('inf'))]
        
        ans = [[0, 0]]
        
        
        for L, NegH, R in events:
            
            if NegH: heapq.heappush(heap, (NegH, R))
            
            while heap[0][1] <= L:
                heapq.heappop(heap)
                
            if ans[-1][1] != -heap[0][0]:
                ans.append([L, -heap[0][0]])
        
        return ans[1:]
    