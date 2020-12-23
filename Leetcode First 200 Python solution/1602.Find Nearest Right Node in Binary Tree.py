
# Find Nearest right Node in Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
    

class Solution:
    def findNearestRightNode(self, root, TreeNode, u: TreeNode):
        
        # bfs solution
        stack = []
        
        stack.append(root)
        
        while stack:
            max_len = len(stack)
            for i in range(len(max_len)):
                
                node = stack.pop(0)
                if not == u: return stack[0] if stack and i != max_len - 1 else None
                
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        
        return None

# o(N) time complexity
# o(N) space complexity

