class Solution:
    def countNodes(self, root: TreeNode) -> int:

        self.count = 0
        def dfs(root):
            if not root: return 
            self.count += 1
            if root.left:
                dfs(root.left)
            
            if root.right:
                dfs(root.right)
    
        dfs(root)
        return self.count

# o(N)
# o(1)