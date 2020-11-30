class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialization for the parent array
        parent = [i for i in range(n)]
        res = n

        # iterate the edges array
        for u, v in edges:
            x = self.find(u)
            y = self.find(v)
            if x != y:
                # union
                # be aware of that Union the root node
                parent[x] = y
                res -= 1
        return res
    
    def find(self, parent, x):
        # This iteration will have a lot of steps
        # choose the next-generation skip iteration
        while parent[x] != x:
            x = parent[x]
        return x

    def find(self, parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
        return x
    
    # use the recursion to find the root

    def find(self, parent, x):
        if parent[x] != x:
            x = find(self, parent, x)
        return x

# time complity o(n)
# space complexity o(m)