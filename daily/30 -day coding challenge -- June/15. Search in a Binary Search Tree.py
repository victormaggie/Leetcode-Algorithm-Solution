class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root: return
        node = root

        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            elif node.val < val:
                node = node.right
        
        return None
    
# binary search logn time complexity
# space complexity o(1)

