class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals or not intervals[0]: return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        intervals = sorted(intervals)
        count = 1
        if len(intervals) == 1: return count
        for i in range(0, len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                count += 1

        
        return count

# test case [[9,10],[4,9],[4,17]]

