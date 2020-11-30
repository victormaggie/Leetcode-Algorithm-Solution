def pair_with_targetsum(arr, target_sum):
    # this is sorted array 
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target_sum:
            return [left, right]
        elif arr[left] + arr[right] == target_sum:
            right -= 1
        elif arr[left] + arr[right] < target_sum:
            left += 1
    return [-1, -1]

# this function can be do like binary search --> N*logN

# the two pointer solution will be o(N)
# space complexity o(1)

# another solution will be hash_table

def pair_with_targetsum(arr, target_sum):
    num = {}
    for i in range(len(arr)):
        diff = target_sum[i]
        if diff not in num:
            num[diff] = i
        else:
            return [num[arr[i]], i]
    return [-1, -1]

# time complexity o(N)
# space complexity o(N)

