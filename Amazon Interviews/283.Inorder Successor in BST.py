class Solution:
    def inorderSuccessor(self, root, p):

        self.count = float('inf')
        self.node = 0
        self.flag = True

        def inorder(root):
            if root == p: self.count = root.val

            inorder(root.left)
            if root.val > self.count and self.flag:
                self.node = root
                self.flag = False
                return
            inorder(root.right)

            return self.node

# o(n)
# o(n) 