class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def binaryTreePaths(self, root):
        if not root: return
        res = []
        path = ""
        self.dfs(root, res, path)
        return res
    
    def dfs(self, root, res, path):
        path = path + str(root.val) + '->'
        if not root.left and not root.right:
            res.append(path[:-2])
            return
        if root.left:
            self.dfs(root.left, res, path)
        
        if root.right:
            self.dfs(root.right, res, path)

