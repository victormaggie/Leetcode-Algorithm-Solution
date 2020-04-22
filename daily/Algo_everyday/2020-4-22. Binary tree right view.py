class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def rightSideView(self, root):
        self.res = []
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, level):
        if not root: return []
        if len(self.res) == level:
            self.res.append(root.val)
        
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)
        