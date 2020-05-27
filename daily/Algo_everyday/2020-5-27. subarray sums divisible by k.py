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
            hashmap[prefixmode] += 1
        return count

# time complexity o(n)
# space complexity o(n)
