class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        
        return self.dfs(1, n)

    def dfs(self, min_val, max_val):

        # stop condition
        if min_val > max_val:
            return [None]
        res = []
        for i in range(min_val, max_val+1):
            left = self.dfs(min_val, i-1)
            right = self.dfs(i+1, max_val)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)

        return res

# recursion method