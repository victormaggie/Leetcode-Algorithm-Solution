class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root):
        # Flatten binary search tree
        self.stack = []
        curr = root
        while curr:
            self.stack.append(curr)
            curr = curr.left
    
    def next(self):
        if self.stack:
            node = self.stack.pop()
        if node.right:
            curr = node.right
            while curr:
                self.stack.append(curr)
                curr = curr.left
        return node.val
    
    def hasNext(self):
        return len(self.stack) > 0

# time complexity o(N)
# space complexity o(N)




