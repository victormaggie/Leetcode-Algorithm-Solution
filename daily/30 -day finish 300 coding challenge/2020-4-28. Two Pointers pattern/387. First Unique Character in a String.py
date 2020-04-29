class Solution:
    def firstUniqChar(self, s):
        arr = collections.Counter(s)
        for idx, char in enumerate(s):
            if arr[char] == 1:
                return idx
        return -1

# time complexity o(N)
# space complexity o(N)
