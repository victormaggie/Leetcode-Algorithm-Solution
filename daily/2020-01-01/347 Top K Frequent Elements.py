# Happy New Year, wish everything will be fine with you.

class Solution(object):
    def topKFrequent(self, nums, k):
        import collections
        import heapq

        hash_map = collections.defaultdict(int)
        # define size
        res = [-float('inf')] * k
        heapq.heapify(res)

        for i in nums:
            hash_map[i] += 1
        for i in hash_map:
            heapq.heappushpop(res,(hash_map[i]), i )

        return [i[i] for i in res]

# time complexity (k o(n^2))
# space complexity (o(m + k))

    def topKFrequent2(self, nums, k):
        import collections
        import heapq
        count = collections.Counter(nums).most_common(k)
        return [i[0] for i in count]


    def topKFrequent3(self, nums, k):
        # time complexity o(n)
        import collections
        import heapq
        count = collections.Counter(nums)
        # build a heap time complexity ko(logk)
        return heapq.nlargest(k, count.keys(), key=count.get)

# time complexity o(nlogk)
# space complexity o(n)

