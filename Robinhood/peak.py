import heapq
def deleteMinimalPeaks(arr):

    n = len(arr)
    
    arr.append(-float('inf'))

    prev = [n] + list(range(n))
    next = list(range(1, n+1)) + [0]

    heap = []

    def check_peaks(i):

        if arr[prev[i]] < arr[i] > arr[next[i]]:
            heapq.heappush(heap, (arr[i], i))
    
    for i in range(n):
        check_peaks(i)

    ans = []
    while heap:
        val, idx = heapq.heappop(heap)
        ans.append(val)

        i, j = prev[idx], next[idx]

        prev[j] = i
        next[i] = j

        check_peaks(i)
        check_peaks(j)

    arr.pop()
    return ans


# double linked list
# nice solution

numbers = [2, 7, 8, 5, 1, 6, 3, 9, 4]
print(deleteMinimalPeaks(numbers))

# time complexity o(nlogn)
# space complexity o(n)

