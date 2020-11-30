class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        # base case
        if n == 1: return "0"

        # calculate the complementarty binary
        mask = 2 ** n - 1

        # recursive
        mid = l // 2 + 1

        if k == mid:
            return '1'
        elif k < mid:
            return self.findKthBit(n-1, k)
        else: return str(1 - int(self.findKthBit(n-1, l-k+1)))

# time complexity o(n)
# space complexity o(1)