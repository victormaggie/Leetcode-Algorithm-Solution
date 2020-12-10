
class Solution:
    def longestOnes(self, A, K):
        
        if not A: return 0
        slow = 0
        ans = 0
        
        for fast in range(len(A)):
            if A[fast] == 0: K -= 1
            while K < 0:
                if A[slow] == 0: K += 1
                slow += 1
            ans = max(ans, fast - slow + 1)
        
        return ans

# sliding window solution

                