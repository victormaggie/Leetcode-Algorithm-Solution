class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            if len(self.minHeap) < k:
                heapq.heappush(self.minHeap, num)
                continue
            heapq.heappushpop(self.minHeap, num)
        
    def add(self, val: int) -> int:
        
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        else:
            heappushpop(self.minHeap, val)
        return self.minHeap[0]

# o(nlogK) solution

