class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrder(self, root):
        if not root: return
        stack = [root]
        res = []
        while stack:
            max_len = len(stack)
            temp = []
            for _ in range(max_len):
                node = stack.pop(0)
                temp.append(node.val)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            res.append(temp[:])
        return res

# time complexity o(N)  --> the number of node!!
# space complexity o(N)

