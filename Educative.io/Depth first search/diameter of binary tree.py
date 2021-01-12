

# The solution for a Tree Diameter

class Solution:
    
    def diameterOfBinaryTree(self, root):
        
        if not root: return 0
        
        self.ans = 0
        
        def height(root):
            if not root: return 0
            
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, left + right)
            
            return max(left, right) + 1
        
        height(root)
        return self.ans

class Solution:
    def diameterOfBinaryTree(self, root):
        
        if not root: return 0
        ans = 0
        def dfs(root):
            nonlocal ans
            
            if not root: return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            ans = max(ans, left + right + 1)
            
            return max(left, right) + 1
        
        dfs(root)
        return ans
    
    # tree traversal!
    

class TreeDiameter:
    def __init__(self):
        self.ans = 0
        
    def find_diameter(self, root):
        self.dfs(root)
        return self.ans
    
    def dfs(self, node):
        if not node: return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        diameter = left + right + 1
        
        self.ans = max(self.ans , diameter)
        
        return max(left, right) + 1

# 
    