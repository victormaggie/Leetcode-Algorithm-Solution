class Solution:
    #edge case
    def rearrangeString(self, s, k):
        if k < 1: return s
        hashmap = {}
        for i in s: hashmap[i] = hashmap.get(i, 0) + 1
        maxheap = []
        for key, val in hashmap.items():
            heapq.heappush(maxheap, (-val, key))
        res =[]
        while maxheap:
            curr_cnt, curr_char = heapq.heappop(maxheap)
            res.append(curr_char)
            # apply cache here!
            queue.append((curr_cnt+1, curr_char))
            # the cache avoid the last number
            if len(queue) == k:
                cnt, char = queue.popleft()
                if -cnt > 0: heapq.heappush(maxHeap, (cnt, char))
        # check the cache!
        return ''.join(res) if len(res) == len(s) else ''

