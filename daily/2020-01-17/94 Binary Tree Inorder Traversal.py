class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def isValidBST(self, root):
        """
        binary search tree
        """
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            
            if not helper(node.left, lower, val):
                return False
            
            return True
        
        return helper(root)


# problem solution for this
# cannot pass [0, -1] case!!!
class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        return self.check(root)
        
        
    def check(self, root):
        if not root.left and not root.right:
            return True

        # condition 2
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        # condition 1
        if root.left.val > root.val or root.right.val < root.val:
            return False

        if root.left:
            self.check(root.left)

        if root.right:
            self.check(root.right)
            
        return True
