from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        res = [intevals[0]]
        for i in range(1, len(intervals)):
            left = res.pop()
            right = intervals[i]

            if right[0] > left[1]:
                res.append(left)
                res.append(right)
            else:
                res.append([left[0], max(left[1], right[1])])
        return res
    
# time complexity o(n)
# space complexity o(1)
