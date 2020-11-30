# dfs --> recursion
class Solution:
    def isValidBST(self, root):
        return self.dfs(root)
    
    def dfs(self, root, min_val = -float('inf'), max_val = float('inf')):
        if not root: return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.root(root.left, min_val, root.val) and self.root(root.right, root.val, max_val)

# time complexity o(N)
# space complexity o(N)

#bfs --> iteration
class Solution:
    def isValidBST(self, root):
        if not root: return True
        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            root, lower, upper = stack.pop()
            if not root: continue
            val = root.val
            if val <= lower or val >= upper: return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        
        return True
# time complexity(N)
# space complexity o(N)

