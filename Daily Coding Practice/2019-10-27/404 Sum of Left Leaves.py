# sum of left leaves
# recursion solution for the calculation

class Solution:
    def sumOfLeftLeaves(self, root):
        sum_val = 0
        if root == None: return 0
        if root.left and root.left.left == None and root.left.right ==None:
            sum_val = root.left.sum_val
        return sum_val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)