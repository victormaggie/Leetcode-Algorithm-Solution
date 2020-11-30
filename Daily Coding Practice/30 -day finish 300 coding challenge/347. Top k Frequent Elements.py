class Solution:
    def topKFrequent(self, nums, k):
        arr = collections.Counter(nums)
        return map(lambda x: x[0], arr.most_common(k))

# time complexity o(Nlogn)
# space complexity o(N)
