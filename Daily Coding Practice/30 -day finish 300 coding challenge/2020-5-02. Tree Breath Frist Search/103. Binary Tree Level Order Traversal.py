class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return
        queue = collections.deque()
        res = []
        zigzag = False
        while queue:
            max_len = len(queue)
            temp = []
            for _ in range(max_len):
                node = queue.popleft()
                if zigzag:
                    temp = [node.val] + temp
                else:
                    temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp[:])
            zigzag = not zigzag
        
        return res

# time complexity o(N)
# space complexity o(N)

