class Solution:
    def countBits(self, num:List) -> List[int]:
        res = [0]
        for i in range(1, num +1):
            res.append(res[i>>1] + i&1)
        return res

# time complexity o(n)
# space complexity o(n)