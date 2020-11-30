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

    # this solution only push in the samllest then the heap only
    def kSmallestPairs2(self, nums1, nums2, k):
        import heapq
        heap = []
        def push(i,j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, ([nums1[i] + nums2[j]], i, j))
        
        push(0,0)
        res = []
        while heap and len(res) < k:            
            _, i, j = heapq.heappop(heap)            
            res.append([nums1[i], nums2[j]])
            # push nums2
            push(i, j+1)
            # push nums1
            if j == 0:
                push(i+1, 0)

        return res


