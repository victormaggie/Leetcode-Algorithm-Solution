class Solution:
    def isValidBST(self, root):
        def helper(root, lower = -float('inf'), upper=float('inf')):
            if not node: return True
            val = node.val
            if lower >= val or upper <= val:
                return False
            if not helper(node.right, val, upper): return False
            if not helper(root.left, lower, val): return False
            return True
        return helper(root)

