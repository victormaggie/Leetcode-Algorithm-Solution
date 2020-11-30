class Solution:
    def topKFrequent(self, words, k):
        minHeap = []
        hashmap = {}
        for i in words:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for i in hashmap:
            if len(minHeap) >= k:
                if minHeap[0][0] < hashmap[i]:
                    heapq.heappushpop(minHeap, (hashmap[i], i))
            else:
                heapq.heappush(minHeap, (hashmap[i], i))
        
        return list(map(lambda x: x[1], minHeap))

# time complexity o(Nlogk)
# space complexity o(N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        minHeap = []
        hashmap = {}
        for i in words:
            hashmap[i] = hashmap.get(i, 0) + 1

        # iterate rest
        
        # we need to add the order of the directionary
        count = 0
        for i in hashmap:
            # check the boundary
            if len(minHeap) >= k:
                if minHeap[0][0] < hashmap[i]:
                    heapq.heappushpop(minHeap, (hashmap[i], count, i))
                elif minHeap[0][0] == hashmap[i] and len(minHeap[0][2]) > len(i):
                    heapq.heappushpop(minHeap, (hashmap[i], count, i))
            else:
                heapq.heappush(minHeap, (hashmap[i], count,  i))
            count += 1

# here how to sort the array!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        prev = ''
        prev_freq = -float('inf')
        res = []
        while minHeap:
            freq, count, char = heapq.heappop(minHeap)
            if prev_freq == freq:
                while len(char) > len(prev):
                    res.pop()
                    res.append(char)
                    res.append(prev)
            else:
                res.append(char)
                prev = char
                prev_freq = freq     
        
        print(res)
        return res[::-1]

# time complexity o(Nlogk)
# space complexity o(N)


###########################################################################################################

# TAKE AWAY:
# heapify is o(N) algortim 
# if use MaxHeap to pop the smallest value

class Solution:
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        # here the same frequent --> how heap restore and pop >??????????????????
        return [heapq.heappop(heap)[1] for _ in range(k)]

# time complexity o(klogN)
# space complexity o(n)

