class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        minheap = []
        for i in range(k):
            heapq.heappush(minheap, (hashmap[i], i))
        
        for j in range(k):
            if hashmap[j] > minheap[0]:
                heapq.heappush((hashmap[j], j))
        
        return list(map(lambda x: x[1], minheap))

# time complexity o(N + Nlog K)
# space complexity o(N)

