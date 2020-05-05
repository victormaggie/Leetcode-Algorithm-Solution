class Solution:
    def singleNumber(self, nums):
        a , b = 0, 0
        for i in nums:
            a = i ^ a & ~ b
            b = i ^ b & ~ a
        return a | b

# time complexity o(N)
# space complexity o(1)

class Solution:
    def singleNumber(self, nums):
        return ((3*sum(set(nums))) - sum(nums)) // 2

# time complexity o(N)
# space complexity o(N)

# if use hash will also have o(N) and o(N) time / space complexity


class Solution:
    def singleNumber(self, nums):
        seen_once = 0
        seen_twice = 0

        for i in nums:
            seen_once = seen_once ^ i & ~ seen_twice
            seen_twice = seen_twice ^ i & ~ seen_once
        # return exact once
        return seen_once | seen_twice

# time complexity o(N)
# space complexity o(1)


