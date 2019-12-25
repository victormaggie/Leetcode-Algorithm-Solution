class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums)[-k]

# Time complexity o(nlog(n))
# space complexity o(1)

    # python solution 2 using heap
    def findKthLargest1(self, nums, k):
        import heapq
        heapq.heapify(nums)
        return heapq.nlargest(k, nums)[-1]
# Time complexity o(nlog(k))
# space complexity o(k)

