class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        res = []
        if not root:
            return
        path = str(root.val)
        self.dfs(root, res, path)
        return res
    
    def dfs(self, root, res, path):
        if not root.left and not root.right:
            res.append(path)
            return 
        
        if root.left:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right:
            self.dfs(root.right, res, path + '->' + str(root.right.val))

# time complexity o(N) --> go through all the node
# space complexity o(N)
