class Solution:
    def maxPathSum(self, root):
        self.res = -float('inf')
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # here is pretty smart -- prune the negative value !!
        
        self.res = max(self.res, root.val + max(left, 0) + max(right, 0))
        return root.val + max(left, right ,0)
    
    # time complexity o(N)
    # space complexity o(H) recursion stack!
