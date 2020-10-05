class Solution:
    def maximumAverageSubtree(self, root):
        def not root: return 0.0

        def dfs(root, max_val, count):

            if not root: return [0, 0, 0]

            left_val = dfs(root.left, max_val, count)
            right_val = dfs(root.right, max_val, count)

            total = left_val[0] + right_val[0] + root.left_val
            count = left_val[1] + right_val[1] + 1
            average = max(left_val[2], right_val[2], total/count)

            return [total, count, average]
        
        return dfs(root, 0, 0)[2]

# time complexity o(n)
# space complexity o(n)

