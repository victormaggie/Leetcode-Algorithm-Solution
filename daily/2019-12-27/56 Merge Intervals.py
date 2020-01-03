class Solution:
    def merge(self, intervals):
        start = []
        end = []
        res = []
        for i in intervals:
            start.append(i[0])
            end.append(i[-1])
        
        start = sorted(start)
        end = sorted(end)
        m = 0
        while m < len(start):
            temp = []
            temp.append(start[m])
            while m < len(start) -1 and start[m+1] <= end[m]: m += 1
            temp.append(end[m])
            m += 1
            res.append(temp)
        return res
