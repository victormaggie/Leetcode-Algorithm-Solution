class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence(self, root, arr):
        if not arr or not root: return False
        return self.dfs(root, arr, 0)
    def dfs(self, root, arr, n):
        if not root: return
        if root.val != arr[n]: return False
        if n == len(arr)-1:
            if not root.left and not root.right: return True
            else: return False
        
        return self.dfs(root.left, arr, n+1) or self.dfs(root.right, arr, n+1)

# time complexity o(n)
# space complexity o(1)

