
# Smallest subtree with all the Deepest Nodes

# Given the root of a binary tree, the depth of each node is the shortest distance to the root

class Solution:
    def subtreeWithAllDeepest(self, root):
        
        # memorization and make the second traversal
        
        hashmap = {None: -1}
        
        # preorder traversal
        def dfs(root, parent=None):
            if root:
                hashmap[root] = hashmap[parent] + 1
                dfs(root.left, root)
                dfs(root.right, root)
        
        dfs(root)
        
        max_dep = max(hashmap.values())
        
        def answer(root):
            if not root or hashmap.get(root, None) == max_dep:
                return root
            
            L, R = answer(root.left), answer(root.right)
            
            return root if L and R else L or R
        
        return answer(root)
        

class Solution:
    def subtreeWithAllDeepest(self, root):
        
        Result = collections.namedtuple("Result", ("node", "dist"))
        
        def dfs(root):
            if not root: return Result(None, 0)
            
            L, R = dfs(root.left), dfs(root.right)
            
            if L.dist > R.dist: return Result(L.node, L.dist+1)
            if L.dist < R.dist: return Result(R.node, R.dist+1)
            
            return Result(root, L.dist+1)
        
        return dfs(root).node
        