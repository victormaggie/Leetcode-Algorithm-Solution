class Solution:
    def frequencySort(self, s):
        hashmap = {}
        for i in s: hashmap[i] = hashmap.get(i, 0) + 1
        arr = []
        [heapq.heappush(arr, (-hashmap[i], i)) for i in hashmap]
        res = ''
        while arr:
            frequency, alpha = heapq.heappop(arr)
            res += alpha * (-frequency)
        return res
    
# time complexity (o(n + nlogk))
# space complexity o(n)

    # the lazy solution
    def frequencySort(self, s):
        counts = collections.Count(s)

        # build up the string
        string_builder = []
        for letter, freq in counts.most_common():
            string_builder.append(letter * freq)
        return ''.join(string_builder)

# time complexity o(n + klogk)
# space complexity o(n)

## Multiset and Bucket Sort
    def frequencySort(self, s):
        if not s: return s

        # hashmap
        counts = collections.Counter(s)
        # get the max one
        max_freq = max(counts.values())
        # bucket sort the characters by frequencies
        buckets = [[] for _ in range(max_freq+1)]

        for c, i in counts.items():
            buckets[i].append(c)
        
        # build up the string
        string_builder = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)
        return ''.join(string_builder)

# time complexity o(N)
# space complexity o(N)
