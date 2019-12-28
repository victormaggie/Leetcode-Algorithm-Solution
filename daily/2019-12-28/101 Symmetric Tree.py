class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left, right):
        if not left and not right:
            return True
        
        if not left or not right:
            return False
        return (left.val == right.val) and self.helper(left.right, right.left) and self.helper(left.left, right.right)

