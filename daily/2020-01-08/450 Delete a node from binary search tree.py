# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        
        # edge case 
        if not root:
            return
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)   
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # if found the value
            if root.left and root.right:
                tmp = self.findMin(root.right)
                root.val = tmp.val
                root.right = self.deleteNode(root.right, tmp.val)
            else:
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left

        return root 
    
    def findMin(self, root):
        while root.left:
            root = root.left
        return root
    