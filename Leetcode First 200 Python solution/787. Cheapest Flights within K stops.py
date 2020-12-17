        
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		G = collections.defaultdict(dict)
        for start, end, price in flights:
            G[start][end] = price
        heap = [[0, src, K+1]]
        while heap:
            price, node, k = heapq.heappop(heap)
            if node == dst:
                return price
            if k > 0:
                for n in G[node].keys():
                    heapq.heappush(heap, [price+G[node][n], n, k-1])
        return -1

