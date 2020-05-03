class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            max_len = len(queue)
            sum, num = 0, 0
            for _ in range(max_len):
                node = queue.popleft()
                sum += node.val
                num += 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(round(sum/num,2))
        return res

# time complexity o(N)
# space complexity o(N)
