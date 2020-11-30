
# binwise manipulation
class Solution:
    def findMaximumXOR(self, nums):

        ans = mask = 0
        for x in range(32)[::-1]:
            mask += 1 << x
            prefixSet = set([n & mask for n in nums])

            temp = ans | 1<<x
            for prefix in prefixSet:
                if temp ^ prefix in prefixSet:
                    ans = temp
                    break
        return ans