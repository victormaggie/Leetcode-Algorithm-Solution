









# Longest Happy String
class Solution:
    def longestDiverseString(self, a, b, c):
        if not a and not b and not c:
            return ""
        
        res = ""
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap.heapify(heap)

        prev_val = 0
        prev_char = ''
        while heap:
            v, char = heapq.heappop(heap)
            if prev_val < 0:
                heapq.heappush(heap, (prev_val, prev_char))
            
            if abs(v) >= 2:
                if abs(v) > abs(prev_val):
                    res += char * 2
                    v += 2
                else:
                    res += char
                    v += 1
            elif abs(v) == 1:
                res += char
                v += 1
            
            elif abs(v) == 0:
                break
            prev_val = v
            prev_char = char
        
        return res
        