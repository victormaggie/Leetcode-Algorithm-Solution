class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return
        root = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:index+1], inorder[:index+1])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
    
    # recursion solution find the root and split the value
    # time complexity o(n)
    # space complexity o(n)