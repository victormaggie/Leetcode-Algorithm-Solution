class Solution:
    def isSameTree(self, p, q):
        # recursion stop condition 1
        if p is None and q is None:
            return True
        
        if p is None: return False
        if q is None: return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        