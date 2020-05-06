class Solution:
    def findClosetElements(self, arr, k, x):
        res = []
        for i in range(len(arr)):
            dist = abs(arr[i] - x)
            if len(res) < k:
                heapq.heappush(res, (-dist, arr[i]))
            else:
                if -res[0][0] > dist:
                    heapq.heappushpop(res, (-dist, arr[i]))

# Analyze the time complexity

class Solution:
    def findClosetElement(self, arr, k, x):
        index = self.binary(arr, x)
        low, high = index-k, index+k
        low = max(0, low)
        high = min(len(arr)-1, high)
        res = []
        for i in range(low, high+1):
            heapq.heappush(res, (abs(arr[i]-x), arr[i]))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(res)[1])
        return sorted(ans)
    

    def binary(self, arr, x):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                right = mid - 1

            else:
                left = mid + 1
        # if cannot find the value
        if low > 0:
            return low - 1
        return left

# time complexity o(logN + klogk)
# space compelxity o(K)
