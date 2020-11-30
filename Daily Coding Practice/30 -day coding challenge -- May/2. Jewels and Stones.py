class Solution:
    def numJewelsInStones(self, J, S):
        jel = set(J)
        count = 0
        for s in S:
            if s in jel: count += 1
        return count

# time complexity o(n)
# space complexity o(n)