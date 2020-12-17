
# Iterate the algorithm --> this is the inorder iteration

class Solution:

    def isValidBST(self, root):
    
        stack, prev = [], -math.inf
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if root.val <= prev:
                return False
            
            prev = root.val
            root = root.right
        
        return True

# o(n) time complexity 
# o(n) space complexity
        
        
# Recursion solution

    def isValidBST(self, root):
        def dfs(root, min_val, max_val):
        
            if not root: return True
            
            if root.val <= min_val or root.val >= max_val:
                return False
            
            return dfs(root.left, min_val, root.val) and dfs(root.right, root.val, max_val)
    
# o(n) time complexity
# o(n) time complexity
