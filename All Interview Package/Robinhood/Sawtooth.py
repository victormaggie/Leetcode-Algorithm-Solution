def countSawSubarrays(array):

    # iteration
    ans = 0
    if not array or len(array) < 2:
        return 0
    
    n = len(array)
    large_th_pre = [0] * n
    small_th_pre = [0] * n

    res = 0

    for i in range(1, len(array)):
        num = array[i]
        if num == array[i-1]:
            continue
        elif num > array[i-1]:
            subcnt = 1
            if i - 2 >= 0 and small_th_pre[i-1] > 0:
                subcnt += 1
                subcnt += large_th_pre[i-2]
            large_th_pre[i] = subcnt
            res += large_th_pre[i]
        else:
            subcnt = 1
            if i - 2 >= 0 and large_th_pre[i-2] > 0:
                subcnt += 1
                subcnt += small_th_pre[i-2]
            small_th_pre[i] = subcnt
            res += small_th_pre[i]

    return res

arr = [2, 7, 5, 6, 1,8]

print(countSawSubarrays(arr))




