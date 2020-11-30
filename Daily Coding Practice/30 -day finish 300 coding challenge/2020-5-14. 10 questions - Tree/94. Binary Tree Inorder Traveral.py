class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        res = []
        def dfs(root, res):
            if not root: return
            if root.left: dfs(root.left, res)
            res.append(root.val)
            if root.right: dfs(root.right, res)
        dfs(root, res)
        return res

# time complexity o(n)
# space complexity o(n)


# Iteratively solve this problem
class Solution:
    def inorderTraversal(self, root):
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res

# time complexity o(n)
# space complexity o(n)
