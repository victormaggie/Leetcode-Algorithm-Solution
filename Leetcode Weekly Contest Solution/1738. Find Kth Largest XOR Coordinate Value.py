class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        
        
        heap = []
        memo = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                
                dp[i][j] = matrix[i-1][j-1] ^ dp[i-1][j] ^ dp[i][j-1] ^ dp[i-1][j-1]
                
                if len(heap) < k:
                    heapq.heappush(heap, dp[i][j])
                    continue
                
                heapq.heappushpop(heap, dp[i][j])
        

        return heap[0]