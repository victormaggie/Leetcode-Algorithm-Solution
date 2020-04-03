# brute force

class Median:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] > num:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -heappop(self.minHeap))
    
    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        

class Solution:
    
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        for i in range(k-1, len(nums)):
            find_median = Median()
            for j in range(i-k+1, i+1):
                find_median.addNum(nums[j])
            res.append(find_median.findMedian())
        return res

        # over the time limit need optimize
        # optimization



class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
    
    def find_sliding_window_median(self, nums, k):
        for i in range(0, len(nums)):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])
            
            self.rebalance_heaps()

            # here is the sliding window for the calculations
            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i-k+1] = (-self.maxHeap[0] + self.minHeap[0]) / 2.
                else:
                    result[i-k+1] = -self.maxHeap[0]/1. 
            
            # remove the element going out of the slide window
            elementToBeRemoved = nums[i - k + 1]
            if elementToBeRemoved <= -self.maxHeap[0]:
                self.remove(self.maxHeap, -elementToBeRemoved)
            else:
                self.remove(self.minHeap, elementToBeRemoved)
            
            self.rebalance_heaps()
        return result
    
    def remove(self, heap, element):
        ind = heap.index(element)
        # move the element to the end and delete it
        heap[ind] = heap[-1]
        del heap[-1]

        # we can use heapify to readjust the element but that wound be o(n)
        # instead, we will adjust only one element which will o(logN)
        
        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)
    
    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.maxHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    # time complexity o(N * k)  array and slide windown   --> insert and removing number from heap o(logk) --> remove out of slide windwon o(k)
    # removing the element going out of the sliding windown, and this will take o(K)

    # Space complexity o(K)

    