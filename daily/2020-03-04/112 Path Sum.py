class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        res = []
        if not root:
            return False

        return self.helper(root, sum, res) or self.hasPathSum(root.left, sum, res) or self.hasPathSum(root.right, sum, res)
        

    def helper(self, root, sum, res):
        
        if not root:
            return sum(root) == sum

        return self.helper(root.left, sum, res.append(root.val)) or self.helper(root.right, sum, res.append(root.val))


