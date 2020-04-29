class Solution:
    def triplet_with_smaller_sum(arr, target):
        arr.sort()
        triplets = []
        N = len(arr)
        for t in range(N):
            i, j = t+1, N-1
            while i < j:
                temp = arr[i] + arr[j] + arr[t]
                if temp < target:
                    for k in range(i+1, j+1):
                        triplets.append([arr[t], arr[i], arr[k]])
                left += 1
                else:
                    right -= 1 
# sorted algorithm o(N*logN)   ---> for loop o(N^3)  
# time complexity o(N^3)
# space complexity o(N)

