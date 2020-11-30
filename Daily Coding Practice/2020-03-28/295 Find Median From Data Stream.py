class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    
    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] > num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        # check the balance

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
        
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return -self.maxHeap[0] / 2. + self.minHeap[0] / 2.
        else:
            return -self.maxHeap[0] /1.

# time complexity for insertation o(logn)
# time complexity for findmedian o(1)
# space complexity o(N)  store all the number!
