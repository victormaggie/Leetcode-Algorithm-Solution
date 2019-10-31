# Binary Tree Path
# Given a Binary Tree return all root to leaf

class Solution:
    def binaryTreePaths(self, root):
        res = []
        if root == None:
            return
        path = str(root.val)
        self.dfs(root, res, path)
        return res
    
    def dfs(self, root, res, path):
    
        if root.left == None and root.right == None:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left, res, path + '->' + str(root.left.val))
        if root.right:
            self.dfs(root.right, res, path + '->' + str(root.right.val))

# solution 2 use the root as the stop point

class Solution_2:
    def binaryTreePaths(self, root):
        res = []
        if root == None:
            return
        
        self.dfs(root, res, '')
        return res
    
    def dfs(self, root, ans, path):
        if root == None:
            return
        
        if path == '':     # beware that this is not c++ path == none is different path == ''
            path += str(root.val)

        if root.left == None and root.right == None:
            ans.append(path)
            return
        
        else:
            self.dfs(root.left, ans, path + '->'+ str(root.left.val))
            self.dfs(root.right, ans, path + '->' + str(root.right.val))