class Solution:
    def intervalIntersection(self, A, B):
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            left = max(A[i][0], B[j][0])
            right = min(A[i][1], B[j][1])
            if left <= right:
                ans.append([left, right])
            
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res

# time complexity o(n+m)
# space complexity o(n+m)
