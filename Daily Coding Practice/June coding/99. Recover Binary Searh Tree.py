# This question test the Inorder tranversal of binary search tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class recoverTree(self, root: TreeNode) -> None:
    current = root
    x = y = predecessor = pred = None

    while current:
        if not current.left:
            if pred and pred.val > current.val:
                y = current
                if x is None:
                    x = pred
            pred = current
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right
            
            # if predecessor.right = None
            if predecessor.right == None:
                predecessor.right = current
                current = current.left
            else:
                if pred and pred.val > current.val:
                    y = current
                    if x is None:
                        x = pred
                predecessor.right = None
                pred = current
                current = current.right
    
    x.val, y.val = y.val, x.val

# time complexity o(n)
# space complexity o(1)

# be aware of Morris traversal
# be sure using inorder traversal and comparision
