
class Solution:

    def sumRootToLeaf(self, root: TreeNode) -> int:

        if not root: return 0

        self.sum = 0

        def dfs(root, path):

            if not root.left and not root.right:
                self.sum += int(path, 2)
                return 

            if root.left:
                dfs(root.left, path + str(root.left.val))

            if root.right:
                dfs(root.right, path + str(root.right.val))
        
        dfs(root, str(root.val))

        return self.sum

# time complexity o(n)
# space complexity o(n)

