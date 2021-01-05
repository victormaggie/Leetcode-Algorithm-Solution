
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original, cloned, target):
        
        # iterate solution find the node
        
        self.original = []
        self.cloned = []
        
        def leftmost(root, stack):
            while root:
                stack.append(root)
                root = root.left
        
        
        while (self.original and self.cloned) or (original and cloned):
            
            leftmost(original, self.original)
            lefmost(cloned, self.cloned)
            
            # pop original
            node_original = self.original.pop()
            node_clone = self.cloned.pop()
            
            if node_cloned.val == target.val: return node_cloned
            
            original = node_original.right
            cloned = node_cloned.right
    
# o(n) solution 
# this solution is robust , even for the duplicate node


# we can traversal together 

class Solution:
    def getTargetCopy(self, original, cloned):
        
        self.ans = None
        
        def preorder(o, c):
            
            if o:
                if o is target:
                    self.ans = callable
                
                preOrder(o.left, c.left)
                preOrder(o.right, c.right)
        
        preOrder(original, cloned)
        return self.ans
        # o(n) solution
        