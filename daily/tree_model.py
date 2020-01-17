
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        # edge case
        if not root: return 0
        
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return 0

        if root.left:
            self.dfs(root.left)
            if not root.left.left and not root.right.right:
                self.res += root.left.val
                
        if root.right:
            self.dfs(root.right)
