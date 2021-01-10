
class TreeNode:
    
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left  = None
    

class Solution:
    
    def hasPathSum(self, root, sum):
        if not root: return 
        
        # check the leaf ans sum path == val
        if root.val == sum and not root.right and not root.left:
            return True
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
# o(n) time complexity


    def bfs(self, root, sum):
    
        if not root: return False
        
        queue = [(root, sum)]
        
        while queue:
            
            (node, val) = queue.pop(0)
            
            if val == node.val and not node.right and not node.left:
                return True
            
            if node.left: queue.append((node.left, val - node.val))
            if node.right: queue.append((node.right, val - node.val))
        
        return False

# o(n) time complexity

# memorize the path sum, and use DFS or BFS traversal