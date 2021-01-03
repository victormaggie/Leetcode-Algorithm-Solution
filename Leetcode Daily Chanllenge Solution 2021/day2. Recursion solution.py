
# DFS recursive inorder traversal

# in order traversal : left -> Node -> right

# use the parallet traversal
class Solution:
    def getTargetCopy(self, original, cloned, target):
        
        def inorder(o, c):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.ans = c 
                inorder(o.right, c.right)
        
        inorder(original, cloned)
        return self.ans

# here is the inorder traversal nice

# preOrder traversal!
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.ans = None
        def preOrder(o, c):
            
            if o:
                
                if o is target:
                    self.ans = c
                
                preOrder(o.left, c.left)
                preOrder(o.right, c.right)
        
        preOrder(original, cloned)
        return self.ans