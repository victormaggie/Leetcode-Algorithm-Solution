class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        if not s: return
        if s.val == t.val and self.check(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def check(self, s, t):
        if t == None and s == None: return True
        if not s or not t: return False
        if s.val != t.val: return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

