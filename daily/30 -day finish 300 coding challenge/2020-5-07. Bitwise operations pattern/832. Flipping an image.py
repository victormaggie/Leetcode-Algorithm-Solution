class Solution:
    def flipAndInvertImage(self, A):
        m, n = len(A), len(A[0])
        for i in range(m):
            A[i] = A[i][::-1]
            for j in range(n):
                A[i][j] ^= 1
        return A

# time complexity o(M+N)
# space complexity o(1)
