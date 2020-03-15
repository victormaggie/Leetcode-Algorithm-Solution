# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        self.storeBSTNodes(root, self.nodes)
        
        n = len(self.nodes)
        return self.buildTreeUtil(self.nodes, 0, n-1)

    
    # in order tranversal
    def storeBSTNodes(self, root, nodes):
        if not root:
            return
        
        self.storeBSTNodes(root.left, nodes)
        self.nodes.append(root)
        self.storeBSTNodes(root.right, nodes)
        
    
    def buildTreeUtil(self, nodes, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        node = nodes[mid]
        
        # left and right subtree
        node.left = self.buildTreeUtil(nodes, start, mid-1)
        node.right = self.buildTreeUtil(nodes, mid+1, end)
        return node


    class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop(-1)
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) < k:
            
            self.stack = list(map(lambda x: x+val, self.stack))
        else:
            for j in range(k):
                self.stack[j] += val
    
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0 and len(matrix[0]) == 0:
            return
        
        return self.dfs(matrix, 0, 0)
        
    def dfs(self, matrix, i, j):
        num_row = len(matrix)
        num_column = len(matrix[0])
        
        if matrix[i][j] == min(matrix[i][:]) and matrix[i][j] == max(matrix[:][j]):
            return [matrix[i][j]]
        
        for i in range(num_row):
            for j in range(num_column):
                self.dfs(matrix, i+1, j)
                self.dfs(matrix, i, j+1)



