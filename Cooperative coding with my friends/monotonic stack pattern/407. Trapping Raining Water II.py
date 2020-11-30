class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        if not heightMap or not heightMap[0]: return 0

        seen = set()
        heap = []
        m, n = len(heightMap), len(heightMap[0])

        for i in range(n)