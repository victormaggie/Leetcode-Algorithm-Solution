class Solution:
    def maxSlidingWindow(self, nums: List[int], k:int) -> List[int]:
        if not nums: return []
        hashmap = collections.defaultdict(int)
        res = []
        for i in range(len(nums)):
            if i < k:
                hashmap[nums[i]] += 1
                continue
            res.append(max(hashmap))
            left_val = nums[i-k]
            if hashmap[left_val] == 0:
                del hashmap[left_val]
            hashmap[nums[i]] += 1
        res.append(max(hashmap))
        return res

# time complexity: o(nk)
# space complexity: o(k)
# 9000ms  omfg!

    def maxSlidingWindow(self, nums: List[int], k:int) -> List[int]:
        if not nums: return []
        for i in range(len(nums)):
            if len(heap) < k:
                heapq.heappush(heap, -nums[i])
                if len(heap) == k:
                    res.append(-heap[0])
                continue
                
            heap.remove(-nums[i-k])
            heapq.heapify(heap)
            heapq.heappush(heap, -nums[i])
            res.append(-heapp0)
        return res 
# time complexity: o(n*k*logk)
# space complexity: o(n)
# ETL  omfg!

    def maxSlidingWindow(self, nums: List[int], k:int) -> List[int]:
        if not nums: return []

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1: return nums
        # restore the number of the idx
        def clean_deque(i):
            if queue and deq[0] == i - k: queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
        
        # init deque and output
        queue = deque()
        output = []
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            queue.append(i)
        output.append(queue[0])

        for j in range(k, len(nums)):
            clean_deque(i)
            queue.append(i)
            output.append(nums[queue[0]])
        return output

# time complexity: o(n)
# space complexity: o(n)

