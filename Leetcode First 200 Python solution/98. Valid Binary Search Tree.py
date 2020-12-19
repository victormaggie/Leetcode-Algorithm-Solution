
class Solution:
	def isValidBST(self, root):
		
		if not root: return False
		
		def dfs(root, min_val, max_val):
			if not root: return True
			if root.val >= max_val or root.val <= min_val: return False
			
			left = dfs(root.left, min_val, root.val)
			right = dfs(root.right, root.val, max_val)
			
			return left and right
	
		return dfs(root, -math.inf, math.inf)

# recursion solution

