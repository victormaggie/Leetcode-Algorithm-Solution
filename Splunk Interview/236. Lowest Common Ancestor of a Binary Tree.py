class Solution:
    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):
            if not current_node:
                return False
            
            if current_node == p or current_node == q:
                return current_node

            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            if left and right: return current_node

            return left or right

        return recurse_tree(root)

        # o(n) complexity
        
