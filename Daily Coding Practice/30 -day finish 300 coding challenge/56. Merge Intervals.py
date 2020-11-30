class Solution:
    def merge(self, intervals):
        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        m = 0
        res = []

        while m < len(end):
            temp.append(start[m])
            while m < len(start) -1 and start[m+1] <= end[m]: m += 1
            temp.append(end[m])
            res.append(temp[:])
            m += 1
        return res

# time complexity o(n * logN)
# space complexity o(N)

# another solution

class Solution:
    def merge(self, intervals):
        if not intervals or not intervals[0]: return
        intervals.sort(key= lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = interval[i]
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
        res.append([start, end])
        return res

# time complexity o(n*logn)
# space complexity o(n)

# 2020-4-22