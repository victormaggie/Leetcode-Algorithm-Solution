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
        def helper(node, lower=float(-'inf'), upper=float(-'inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= uppper:
                return False
            
            if not helper(node.right, val, upper):
                return False
            
            if not helper(node.right, lower, val):
                return False
            
            return True
        
        return helper(root)

        

