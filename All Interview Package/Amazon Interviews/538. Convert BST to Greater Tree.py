class Solution:
    def postorder(root):
        if not root: return

        if root.right: postorder(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left: postorder(root.left)
        return root
    return postorder(root)

# o(n)
# o(n)

# bfs solution:

    def postorder(root):
        total = 0
        node = root
        stack = []

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.right
            
            node = stack.pop()
            total += node.val
            node.val = total

            node = node.left
    
        return root

# time complexity o(n)
# space complexity o(n)

