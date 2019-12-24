class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def invertTree(self, root):

        # edge case
        if not root:
            return

        # every level we need swap

        temp = root.left
        root.left = root.right
        root.right = temp

        # recursion

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# time complexity o(n)

"""
Google: 90% of our engineers use the software you wrote (Homebrew), 
but you can’t invert a binary tree on a whiteboard so f*** off.
"""