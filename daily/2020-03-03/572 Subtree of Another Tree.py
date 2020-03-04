class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        # edge case
        if s is None and t is None:
            return True
        if t is None: return True
        if s is None: return False
        
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSame(self, p, q):
        if p is None and q is None:
            return True
        if p is None: return False
        if q is None: return False

        return p.val == q.val and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)
    

    def isSubtree2(self, s, t):
        if not s and not t: return True
        if not t: return True
        if not s: return False

        return self.isSame(s,t) or self.issubtree(s.left, t) or self.issubtree(s.right, t)

    
    def isSame2(self, p, q):
        if not p and not q: return True
        if not p: return False
        if not q: return False

        return p.val == q.val and self.isSame2(p.left, q.left) and self.isSame2(p.right, q.right)

        
