class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            max_len = len(queue)
            stack = []
            for _ in range(queue):
                node = queue.popleft()
                stack.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(stack)
        return res

# Bfs o(N)
# space complexity o(N)

# we can also solve this question by depth first search!
class Solution:
    def levelOrder(self, root):
        if not root: return []
        res = []
        def dfs(root, level):
            if level == len(res):
                res.append([])
            
            # append the current node value
            # asign the val to each level
            res[level].append(node.val)
            if node.left: dfs(root, level+1)
            if node.right: dfs(root, level+1)

    dfs(root, 0)
    return res 
