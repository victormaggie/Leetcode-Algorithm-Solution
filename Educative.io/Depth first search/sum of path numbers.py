

# Find sum of path number

def find_sum_of_path_numbers(root):
    
    if not root: return 0
    
    def dfs(root, pathSum):
        
        if not root: return 0
        
        # add the value here
        pathSum = pathSum * 10 + root.values
        
        # if we found the leaf node
        if not root.left and not root.right: return pathSum
        
        # let us search the left value
        left = dfs(root.left, pathSum)
        right = dfs(root.right, pathSum)
        
        return left + right
    
    return dfs(root, 0)

# this is not need the path output, we do not need to do backtracking
