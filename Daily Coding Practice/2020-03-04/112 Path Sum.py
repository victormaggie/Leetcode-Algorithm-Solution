class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        
        if not root:
            return False

        return self.dfs(root, sum, root.val)
        

    def dfs(self, root, sum, res):
        
        # check the leaf node
        if not root.left and not root.right and res == sum:
            return True
        
        flag_left, flag_right = False, False

        if root.left:
            self.dfs(root, sum, res + root.left.val)
        
        if root.right:
            self.dfs(root, sum, res + root.right.val )

        return flag_left or flag_right


class Solution2:
    def hasPathSum(self, root, sum):
        if not root: 
            return False
        
        if not root.left and not root.right:
            return sum == root.val
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

        




