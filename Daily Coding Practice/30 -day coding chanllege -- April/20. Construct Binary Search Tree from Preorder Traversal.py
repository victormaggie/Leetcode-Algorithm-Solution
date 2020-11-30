from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        if not root: return 
        self.index = 0
        n = len(preorder)
        return self.dfs(preorder, n)
    
    def dfs(self, preorder, n, min_limit=-float('inf'), max_limit=float('inf'))
        if self.index == n:
            return
        val = preorder[self.index]
        if val <= min_limit or val >= max_limit:
            return
        root = TreeNode(val)
        root.left = self.dfs(preorder, n, min_limit, root.val)
        root.right = self.dfs(preorder, n, root.val, max_limit)
        return root

# time complexity o(N)
