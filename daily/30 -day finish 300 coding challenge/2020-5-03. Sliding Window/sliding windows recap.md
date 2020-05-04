# Sliding window
* This algorithm usually for the calculation of contiguous subarrays.
* Like "Given an array, find the average of all contiguous subarray of size 'K' in it"

```
# the calculation of contiguous sum
# brute force can have the repeat calculation
arr = [1, 3, 2. 6, -1, 4, 1, 8, 2], k = 5

for i in range(len(arr) - (k-1)):
    total_sum = 0.0
    for j in range(i, i+k):
        total_sum += arr[j]
    result.append(total_sum/K)

# time complexity o(N*k)  --> every number and iterate the next k number value
# space complexity o(N)


# the slide window can reduce the calculation into o(N)
result = []
cum_sum = 0
ed_win = 0
for st_win in range(len(arr))
    cum_sum += arr[i]
    st_win += 1
    if st_win - ed_win >= k-1:
        result.append(cum_sum / k)
        cum_sum -= arr[ed_win]
        ed_win += 1
return result

```

* Mutal questions: we will use the question to solve the question for the 
* the window can be mutable and need `expand` or `shrink`


# find the smallest contiguous array sum greater than k
```
def smallest_subarray_with_given_sum(s, arr):
    cum_sum = 0
    min_len = float('inf')
    ed_window = 0
    for st_window in range(0, len(arr)):
        cum_sum += arr[st_window]
        while cum_sum >= k:
            min_len = min(min_len, st_window - ed_window+1)
            cum_sum -= arr[ed_window]
            ed_window += 1 
    if min_len = math.inf
        return 0
    return min_len
# time complexity o(n)
# space complexity o(1)

```