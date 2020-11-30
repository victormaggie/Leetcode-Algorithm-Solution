class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # return condition
        if not root or root == p or root == q: return root
        # traverse the left and right node
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if null return 
        if not left and not right: return
        # if left null ---> return right
        if not left: return right
        # if right null ---> return left
        if not right: return left
        # return root
        return root
# time complexity o(N)
# space complexity o(N)
