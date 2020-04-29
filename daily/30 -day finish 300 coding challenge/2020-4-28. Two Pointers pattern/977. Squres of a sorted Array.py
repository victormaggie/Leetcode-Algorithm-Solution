class Solution:
    def sortedSquares(self, A):
        return sorted(map(lambda x: x**2, A))

# 200 ms
# time complexity o(NlogN)
# space complexity o(N)

class Solution:
    def sortedSquares(self, A):
        left, right = 0, len(A)-1
        square = [0 for _ in range(len(A))]
        max_len = len(A) - 1

        while left <= right:
            val_left = A[left] ** 2
            val_right = A[right] ** 2
            if val_left > val_right:
                square[max_len] = val_left
                left += 1
            else:
                square[max_len] = val_right
                right -= 1
            max_len -= 1
    
        return square
# 273 ms
# time complexity o(N)
# space complexity o(N)

### be aware of that !! python map function has multi-threading calculation  --> usually performance is good

