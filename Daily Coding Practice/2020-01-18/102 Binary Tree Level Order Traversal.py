class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def levelOrder(self, root):
        # bfs search
        if not root: return
        res = []
        path = []
        queue = []
        queue.append(root)
        self.bfs(queue, res, path)
        return res

    def bfs(self, queue, res, path):
        # recursion stop conditions
        if not queue:
            return res
        # define a queue
        k = len(queue)
        path = []
        while k:
            node = queue.pop(0)
            path.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        res.append(path[:])
        self.bfs(queue, res, path)
        
# breath first tranversal 

