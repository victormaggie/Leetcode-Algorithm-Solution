class Solution:
    def lastStoneWeight(self, stones):
        # heap solution
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
    
        while len(stones) > 1:
            num1 = heappop(stones)
            num2 = heappop(stones)
            if num1 == num2:
                continue
            else:
                heapq.heappush(stones, num1 - num2)
        
        return -stones[0] if stones else 0

    # time complexity o(nlogn)
    # space complexity o(n)