class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        def comparison(left, right):
            if not left and not right: return True
            if not left: return False
            if not right: return False
            if left.val != right.val: return False
            return comparison(left.left, right.right) and comparision(left.right, right.left)
        
        return comparision(root.left, root.right)

# time complexity o(N)
# space complexity o(N)
