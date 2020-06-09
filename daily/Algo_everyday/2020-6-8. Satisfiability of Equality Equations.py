class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        class UnionFind:
            # define a class here
            def __init__(self, n):
                self.parent = [i for i in range(n)]
            
            # find the root node for x
            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x
            
            def union(self, x, y):
                root1 = self.find(x)
                root2 = self.find(y)
                if root1 != root2:
                    self.parent[root1] = root2
            
            def is_connected(self, x, y):
                return self.find(x) == self.find(y)
            
        UF = UnionFind(26)
        # find we need find '==' to construct the union
        for equation in equations:
            if equation[1] == '=':
                # change to ascii
                char1 = ord(equation[0]) - ord('a')
                char2 = ord(equation[-1]) - ord('a')

                root1 = UF.find(char1)
                root2 = UF.find(char2)

                UF.union(root1, root2)
        
        for equation in equations:
            if equation[1] == '!':
                # change to ASCii
                char1 = ord(equation[0]) - ord('a')
                char2 = ord(equation[-1]) - ord('a')
                if UF.is_connected(char1, char2): return False
        return True

# time complexity: o(n)
# space complexity: o(n)



