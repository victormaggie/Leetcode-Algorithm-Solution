class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# DFS
class Solution:
    def kthSmallest(self, root, k):
        
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        return inorder(root)[k-1]

# time complexity o(n)
# space complexity o(n)

# BFS
class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.popp()
            k -= 1
            if not k:
                return root.val
            root = root.right

# the height of the tree!
# time complexity o(H + k)
# space complexity o(H + k)