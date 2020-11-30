class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        heap = []
        # use the heap 
        for i in nums:
            heappush(heap, (-i, i))
        
        res = 0
        for _ in range(k):
            res = heappop(heap)[1]
        return res

# this algorithm is Nlog(N)  -> break down the tree is still logN
# space complexity o(logN)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        return heapq.nlargest(k, nums)[-1]
# time complexity: o(nlogk)
# space 