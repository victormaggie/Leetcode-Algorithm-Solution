
# return all the path 

class Solution:
    
    def sumRootToLeaf(self, root):
        if not root: return
        
        self.ans = 0
        
        def dfs(root, val):
            if not root: return
            
            val = val << 1 | root.val
            
            if not root.left and not root.right:
                self.ans += val
            
            else:
                dfs(root.left, val)
                dfs(root.right, val)
            
            val >>= 1
            
        dfs(root, 0)
        
        return self.ans

