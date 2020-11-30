class Solution:
    def subarraysDivByK(self, A: List[int], k: [int]):
        prefixmode = 0
        count = 0
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        for i in range(len(A)):
            prefixmode = (prefixmode + A[i]) % K
            if prefixmode in hashmap:
                count += hashmap[prefixmode]
            # we can use the build-in hashmap attributes
            # when cannot find return 0
            # count += hashmap[prefixmode]
            hashmap[prefixmode] += 1
        return count

# time complexity o(n)
# space complexity o(n)
