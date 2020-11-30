class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or not intervals[0]: return 0
        minHeap = []
        intervals = sorted(intervals)
        count = 0
        for interval in intervals:
            if not minHeap:
                heapq.heappush(minHeap, (interval[1], interval[0]))
            else:
                if minHeap[0][0] <= interval[0]:
                    heapq.heappushpop(minHeap, (interval[1], interval[0]))
                else:
                    heapq.heappush(minHeap, (interval[1], interval[0]))
            count = max(count, len(minHeap))
        return count

# time complexity o(nlogn)
# space complexity o(n)


class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or not intervals[0]: return 0
        minHeap = []
        intervals = sorted(intervals)
        count = 0
        heapq.heappush(minHeap, (intervals[0][1]))
        for interval in intervals[1:]:
            if minHeap[0] <= interval[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, (interval[1]))
        return len(minHeap)
    
# time complexity o(nlogn)
# space complexity o(n)
