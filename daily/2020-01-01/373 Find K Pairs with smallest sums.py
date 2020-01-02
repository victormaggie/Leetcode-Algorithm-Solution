class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        res = []
        if not nums1 or not nums2:
            return res
        
        heap = []
        len1, len2 = len(nums1), len(nums2)

        for x in range(len1):
            heapq.heappush(heap, (nums1[x], nums2[0]), x, 0)
        
        while len(res) < min(k, len1 * len2):
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len2:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res

