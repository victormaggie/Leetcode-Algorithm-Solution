class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root):
        if not root: return
        # define a stack instead of queue
        queue = [(root, 0)]
        res = []
        temp = []
        prev = 0
        while queue:
            node, curr = queue.pop(0)
            if prev != curr:
                res.append(temp[:])
                temp = []
            temp.append(node.val)
            if root.left: queue.append((node.left, curr+1))
            if roor.right:queue.append((node.right, curr+1))
            prev = curr
            # the last element in the stack
            if not queue:
                res.append(temp[:])
        return res[::-1]

# time complexity o(N)
# space complexityO(N)

# Another solution 

class Solution:
    def levelOrderBottom(self, root):
        if not root: return 
        queue = [(root, 0)]
        # queue = collections.deque()
        # queue.append(root)
        res = []

        while queue:
            len_level = len(queue)
            temp = []
            for _ in range(len_level):
                node = queue.pop(0)
                # node = queue.popleft()
                temp.append(node.val)
                if root.left: queue.append(root.left)
                if root.right: queue.append(root.right)
            res = [temp[:]] + res
        return res
# bfs
# time complexity o(N^2)
# space complxity o(N)