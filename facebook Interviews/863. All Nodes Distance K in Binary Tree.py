class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        path = [root]
        self.find_target(root, target, path)
        res = []
        seen = set()
        for node in path[::-1]:          
            self.find_k(node, K, res, seen)
            K -= 1
            seen.add(node)         
        return res
    
    def find_k(self, node, K, res, seen):      
        if node in seen:
            return
        
        if not node:
            return
        if K == 0:
            res.append(node.val)
            return
        
        self.find_k(node.left, K-1, res, seen)
        self.find_k(node.right, K-1, res, seen)
        
        
    def find_target(self, root, target, path):
        if not root:
            return False
        if root == target:
            return True
        
        path.append(root.left)
        if self.find_target(root.left, target, path):
            return True
        path.pop()
        path.append(root.right)
        if self.find_target(root.right, target, path):
            return True
        path.pop()
                    