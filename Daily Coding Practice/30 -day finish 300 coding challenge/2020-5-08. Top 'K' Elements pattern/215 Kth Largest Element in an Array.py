class Solution:
    def findKthLargest(self, nums, k):
        temp = []
        for i in nums: heapq.heappush(temp, -i)
        res = 0
        while k > 0: 
            res = - heapq.heappop(temp) 
            k -= 1
        return res

# time complexity --> generate the heap binary tree o(logN) ---> find the res ---> o(KlogN)
# space complexity o(n)

##### -----> we can still simplify this algorithm

class Solution:
    def findKthLargest(self, nums, k):
        minheap = []
        for i in range(K):
            heapq.heappush(minheap, nums[i])
        # time complexiyt o(Klogk)

        for i in range(k, len(nums)):
            if nums[i] > minheap[0]:
                heapq.heappushpop(nums[i])
        # time complexity o((n-k)logk)
        return list(minheap)

# total time complexity o(nlogk)
# space complexity o(k)

# lazy solution
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)
    
# time coplexity o(NlogK)
# space complexity o(K)



