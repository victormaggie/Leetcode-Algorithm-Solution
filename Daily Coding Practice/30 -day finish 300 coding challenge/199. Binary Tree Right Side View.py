class Solution:
    def rightSideView(self, root):
        self.res = []
        self.dfs(root, 0)
        return self.res
    # this is pretty smart solution
    # jaja!!
    def dfs(self, root, level):
        if not root: return []
        if len(self.res) == level:
            self.res.append(root.val)
        
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)

# we can also use the Breath First search!

class Solution:
    def rightSideView(self, root):
        if not root: return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            max_len = len(queue)
            for i in range(0, max_len):
                currentNode = queue.popleft()
                if i == max_len - 1: res.append(currentNode.val)
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)
        return res

# time complexity o(n)
# space complexity o(n)