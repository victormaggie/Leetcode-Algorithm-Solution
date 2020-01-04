class Solution(object):
    def kClosest(self, points, K):
        import heapq
        if not points:
            return
        heap = []
        for i in points:
            heapq.heappush(heap, (i[0]**2 + i[1]**2, i))
        
        return [i[1] for i in heapq.nsmallest(K, heap)]

# time complexity (m* o(nlogn))
# space complexity o(n)

    def kClosest1(self, points, K):
        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]

## Another solution using Minheap and divide and conquer solution

