class Solution:
    def removeDuplicates(self, S):
        res = []
        for i in S:
            if res and res[-1] == i:
                res.pop()
                continue
            res.append(i)
        return ''.join(res)