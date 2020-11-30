class Solution:
    
    # brute force solution
    def validSquare(p1, p2, p3, p4):

        if not p1 or not p2 or not p3 or not p4: return False

        c = itertools.permutations([p1, p2, p3, p4])

        def helper(a, b, c, d):
            return dist(a, b) > 0 and dist(a, b) == dist(b, c) and dist(b, c) == dist(c, d) and dist(c, d) == dist(d, a)

        for i in c:
            if helper(*i): return True
        return False    


    def validSquare(p1, p2, p3, p4):

        if not p1 or not p2 or not p3 or not p4: return False

        def distance(a, b):
            val = (a[0] - b[0])**2 + (a[1] - b[1])**2
            return val
        
        if distance(p1, p2) != distance(p3, p4)

        def check(a, b, c, d):
            return dist(a, b) > 0 and dist(a, b) == dist(b, c) and dist(b, c) = dist(c, d) and dist(c, d) == dist(d, a)
        
        return check(p1, p2, p3, p4) or check(p1, p3, p2, p4) or check(p1, p2, p4, p3)

# time complexity o(1)
# space complexity o(1)


    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        result = set()
        
        arr = [p1, p2, p3, p4]
        
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):

                if dist(arr[i], arr[j]) == 0:
                    return False
                
                result.add(dist(arr[i], arr[j]))
        
        # use the set, check if there only has a lateral length and 1 diagnal
        return len(result) == 2
