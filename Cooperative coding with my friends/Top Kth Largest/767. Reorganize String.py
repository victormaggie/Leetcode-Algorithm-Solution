class Solution:
    def reorganizeString(self, S: str) -> str:
        
        heap = []
        
        for char in set(S):
            heap.append((-S.count(char), char))
        
        heapq.heapify(heap)

        count, char = heap[0]
        # only need to calculate the largest number, that's it
        # the boundary for the reorganized string is (N + 1) // 2
        if -count > (len(S) + 1) // 2: return ''
        
        ans = []
        while len(heap) >= 2:
            
            num1, char1 = heappop(heap)
            num2, char2 = heappop(heap)
            
            ans.extend([char1, char2])
            
            if num1 + 1: heappush(heap, (num1 + 1, char1))
            if num2 + 1: heappush(heap, (num2 + 1, char2))
        
        return "".join(ans) + (heap[0][1] if heap else "")

# n log K 
# solution