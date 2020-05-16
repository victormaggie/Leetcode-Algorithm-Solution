class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def levelOrder(self, root):
        # omfg !! do not forget the edge case!!
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            max_len = len(queue)
            temp = []
            for _ in range(max_len):
                node = queue.popleft()
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp[:])
        return res

# time compleixity o(n)
# space complexity o(n)

# Binary Tree Zigzag Order Traversal
# Binary Tree Level Order Traveral II
# Minimum Depth of Binary Tree
# Binary Tree Vertical Order Traversal
# Average of Level in Binary Tree
# N-ary Tree Level Order Traversal
# Cousins in Binary Tree

