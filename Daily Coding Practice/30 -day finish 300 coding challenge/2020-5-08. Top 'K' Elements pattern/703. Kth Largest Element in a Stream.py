class KthLargest:
    def __init__(self, k, nums):
        # minHeap otherwise ETL
        self.k = k
        self.minHeap = nums
        heapq.heapify(nums)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
    
    def add(self, val):
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
        else:
            heapq.heappushpop(self.minHeap, val)
        return self.minHeap[0]
