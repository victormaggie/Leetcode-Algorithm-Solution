

class Solution:
    
    def maxPathSum(self, root):
        
        ans = -float('inf')
        
        def dfs(root):
                        
            nonlocal ans
            
            if not root: return 0
            
            left = max(root.val + dfs(root.left), root.val)
            right = max(root.val + dfs(root.right), root.val)
            
            ans = max(ans, left + right - root.val)
            
            return max(left, right)
        
        dfs(root)
        
        return ans
        
            
            