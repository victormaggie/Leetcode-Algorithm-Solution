
# find the continuous value in the array

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        # dfs solution here
        
        # left, right
        
        if not root: return 0

        def dfs(root, target, val):

            if not root: return 0
            
            val += root.val
            
            return (val == target) + dfs(root.left, target, val) + dfs(root.right, target, val)
        
        return dfs(root, sum, 0) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        

class Solution:
    
    def pathSum(self, root, sum):
        
        def preorder(node, curr_sum):
            nonlocal count
            
            if not node: return
            
            curr_sum += node.val
            
            if curr_sum == k:
                count += 1
            
            count += h[curr_sum -k]
            
            h[curr_sum] += 1
            
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            
            h[curr_sum] -= 1
            
        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count
        
    # the prefix sum solution
    