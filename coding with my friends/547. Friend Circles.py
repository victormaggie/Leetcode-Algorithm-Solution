class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        p = [i for i in range(len(M))]

        def find(x):
            if p[x] != x:
                p[x] = find(p[p[x]])
            return p[x]
        
        for i in range(len(M)):
            for j in range(i):
                if M[i][j] == 1:
                    a = find(i)
                    b = find(j)
                    p[a] = b
        
        return len(set(p))

# time complexity o(n2)
# space complexity o(1)


