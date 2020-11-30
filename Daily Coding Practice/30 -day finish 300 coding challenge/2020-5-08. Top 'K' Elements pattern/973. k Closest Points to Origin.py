# the first solution is to use maxheap for the calculation
# time complexity o(nlogk)
# space complexity o(k)
class Solution:
    def kClosest(self, points, K):
        maxheap = []
        for i in range(K):
            dist = sqrt(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(maxheap, (-dist, points[i]))
        
        for i in range(K, len(points)):
            dist = sqrt(points[i][0]**2 + points[i][1]**2)
            if -maxheap[0][0] > dist:
                heapq.heappushpop((-dist, points[i]))
        
        return [i[1] for i in maxheap]

# the lazy solution also o(nlogk)
# space complexity o(n)
    
    def kClosest(self, points, K):
        maxheap = []
        for i in points:
            heapq.heappush(maxheap, (i[0]**2 + i[1]**2, i))
        return heapq.nsmallest(K, maxheap)
