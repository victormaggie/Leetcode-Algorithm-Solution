class Solution(object):

    def findSecondMinimumValue(self, root):
        
        return self.dfs(root, root.val)
    def dfs(self, root, res):
        if not root:
            return -1
        
        if root.val > res: return root.val
        sl = self.dfs(root.left, res)
        sr = self.dfs(root.right, res)

        if sl==-1: return sr
        if sr==-1: return sl
        return min(sl, sr)
