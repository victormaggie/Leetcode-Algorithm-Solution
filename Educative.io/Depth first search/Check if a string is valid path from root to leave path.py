
# LC 1430 :

# the source of the node is from the top
class Solution:
    
    def isValidSequence(self, root, arr):
        
        def dfs(root, idx):
            if not root: return
            
            if root.val != arr[idx]: return False
            
            if idx == len(arr) - 1:
                if not root.left and not root.right: return True
                return False
            
            left = dfs(root.left, idx+1)
            right = dfs(root.right, idx+1)
        
            return left or right
        
        return dfs(root, 0)

# the solution of dfs!