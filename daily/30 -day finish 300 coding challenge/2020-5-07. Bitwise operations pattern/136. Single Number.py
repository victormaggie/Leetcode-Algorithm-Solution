class Solution:
    def singleNumber(self, nums):
        no_duplicate_list = []
        # no_duplicate_list = set()
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
                #no_duplicate_list.add(i)
            else:
                no_duplicate_list.remove(i)
                #no_duplicate_list.remove(i)
        return no_duplicate_list[-1]

# time complexity o(n ^ 2)  --> for loop o(N) --> look up list o(N) ---> 1648 ms
# space complexity o(N)

# hashset time complexity o(N) --> 88 ms
# space complexity o(N)


    def singleNumber(self, nums):
        val = 0
        for i in nums:
            val ^= i
        return val

# time complexity o(n)
# space complexity o(1)


