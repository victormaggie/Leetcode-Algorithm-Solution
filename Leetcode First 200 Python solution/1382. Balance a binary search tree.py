
# 1382. python Balanced a Binary Search tree


class Solution:
    def balanceBST(self, root):
        
        stack = []
        temp = []
        
        # we use the iterate method to traversal the inorder of BST
        while stack or root:
            
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            temp.append(node.val)
            
            root = node.right
            
        
        # we can also use the dfs traversal!
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
            
            
        
        def build(stack):
            
            if not stack: return None
            
            if len(stack) & 1: index = ceil(len(stack)/2)
            else: index = len(stack) // 2
            
            root = TreeNode(stack[:index-1])
            
            if index >= 1:
                root.left = build(stack[:index-1])
                root.right = build(stack[index:])
            
            return root
        
        return build(temp)