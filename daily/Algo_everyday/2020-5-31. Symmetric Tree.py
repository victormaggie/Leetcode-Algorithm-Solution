class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        def helper(root1, root2):
            if not root1 and not root2:
                return True
            if not root1: return False
            if not root2: return False

            if root1.val != root2.val: return False

            comparision1 = helper(root1.left, root2.right)
            comparision2 = helper(root1.right, root2.left)

            return comparision1 and comparision2
        
        return helper(root.left, root.right)

# time complexity o(n)
# space complexity o(n)

