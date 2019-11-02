# Given a binary tree, find its minimum depth

# Tree traversal

"""
 DFS solution: is not efficient, we need use the Breath first search
 DFS : 56 ms. 
 space complexity o(n), small
 disadvantage: cannot handle 10000000 level + 
"""
import collections
class Solution:
    def minDepth(self, root):
        path = 0
        return self.dfs(root, path)

    def dfs(self, root, path):
        if root == None:
            return path
        
        if root.left != None and root.right != None:
            return min(self.dfs(root.left, path+1), self.dfs(root.right, path+1))
        else:
            return max(self.dfs(root.left, path+1), self.dfs(root.right, path+1))

"""
BFS solution: use deque the calculation is 44 ms
BFS use queue
space complexity o(m^n)
advantage: have the MINIMUM quality, queue can store very large item
disadvantage: space large
"""
class Solution2:
    def minDepth(self, root):
        if root == None:
            return 0
        
        queue = collections.deque([(root, 1)])

        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
