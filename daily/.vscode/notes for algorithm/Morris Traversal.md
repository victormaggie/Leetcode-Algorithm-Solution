# Morris Traversal

### Recursive tranversal
def inorder_tranversal(self, node):
    if not root: return
    self.inorder_tranversal(node.left)
    print(root.val)
    self.inorder_tranversal(node.right)

### Morris tranversal
```
def Morris_traversal(self, node):
    current = node
    while current:
        if not current.left:
            print(current.val)
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            # Case 1: Build bridge
            if predecessor.right == None:
                predecessor.right = current
                current = current.left
            else:
            # Case 2: Destroy bridge
                print(current.val)
                predecessor.right = None
                current = current.right

# time complexity o(n)
# space complexity o(1)
```