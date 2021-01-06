
class Solution:

	def generateTrees(self, n):
		
		if n == 0: return []
		
		# This is backtracking solution
        
        return self.helper(1, n)
    
    def helper(self, m, n):
        
        if m > n: return [None]
        
        res = []
        
        for i in range(m, n+1):
            
            left = self.helper(m, i-1)
            right = self.helper(i+1, n)
            
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        
        return res

# o(katlan number)