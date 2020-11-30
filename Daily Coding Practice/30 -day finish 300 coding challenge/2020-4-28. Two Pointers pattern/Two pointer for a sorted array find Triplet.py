class solution:
    def search_triplet(arr):
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]
                continue
            return search_pair(arr, -arr[i], i + 1,  triplets)
    
    def search_pair(arr, target, left,  triplets):
        right = len(arr) - 1
        left = 0
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1

# time complexity o(N * logN) --> sort algorithm  +++++ o(N^2)   ----> O(N^2)
# space complexity o(N)
