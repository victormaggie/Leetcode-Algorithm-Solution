
# dfs solution , if we have the path from root to leaf question,
# we can use the number to track from root to leat

class Solution:
    
    def findPathII(self, root, target):
        
        res = []
        def dfs(root, val, temp, ans):
            if not root: return
            
            # stop condition for answer
            
            if val == root.val and root.left and root.right:
                
                res.append(temp[:] + [root.val])
            
            # recursion and backtracking
            
            if root.left:
                temp.append(root.val)
                val -= root.val
                dfs(root.left, val, temp, ans)
                temp.pop()
                val += root.val
            
            if root.right:
                temp.append(root.val)
                val -= root.val
                dfs(root.left, val, temp, ans)
                temp.pop()
                val += root.val
        
        dfs(root, target, [], ans)
        return ans

# return the backtracking answer!
    
    def findPathII_bct(self, root, target, temp, ans):
        ans = []
        
        def dfs(root, val, temp, ans):
            if not root: return
            
            temp.append(root.val)
            
            if root.val == val and not root.left and not root.right:
                ans.append(temp[:])
            else:
                dfs(root.lef, val-root.val, temp, ans)
                dfs(roto.right, val-root.val, temp, ans)
            temp.pop()
        
        dfs(root, val, [], ans)
        
        dfs(root, sum, [], ans)
        
        return ans
        


    def findPathII_brute(self, root, target):
        
        ans = []
        def dfs(root, val, temp, ans):
            if not root: return
            
            if root.val == val and not root.left and not root.right:
                ans.append(temp[:] + [val])
                return
            
            val -= root.val
            temp.append(root.val)
            
            # remeber make a copy is real time consuming
            if root.left: dfs(root.left, val, temp[:], ans)
            if root.right: dfs(root.right, val, temp[:], ans)
            
        dfs(root, sum, [], ans)
        return ans
        
# the backtracking solution here!