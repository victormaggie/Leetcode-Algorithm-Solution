class Solution:
    def frequencySort(self, s):
        s_count = collections.Counter(s)
        arr = []
        for i in s_count:
            arr.append((i, s_count[i]))
        arr = sorted(arr, key=lambda x: x[1], reverse=True)
        res = ''
        for i in arr:
            res += i[0] * i[1]
        return res

# time complexity o(nlogn)
# space complexity o(n)

    def frequencySort(self, s):
        if not s: return s
        # determine the frequency of each character
        counts = collections.Counter(s)
        max_freq = max(counts.values())
        buckets = [[] for _ in range(max_freq+1)]

        for c, i in counts.items():
            buckets[i].append(c)
        
        # build up the string
        string_builder = []
        for i in range(len(buckets)-1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)
        return "".join(string_builder)

        # determine the frequency

# time complexity o(n)
# space complexity o(n)
