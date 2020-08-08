class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        hashmap = collections.defaultdict(list)
        res = self.dfs(root, hashmap, 0, 0)
        # sort item here
        temp = sorted(res.items())

        ans = []
        for i in res:
            temp = i[1]
            temp = sorted(temp, key=lambda x: (-x[0], x[1]))
            ans.append([node[1] for node in temp])
        return ans
    
    def dfs(self, root, hashmap, idx, idy):
        if not root:
            return
        hashmap[idx].append((idy, root.val))
        # left child
        self.dfs(root.left, hashmap, idx-1, idy-1)
        # right child
        self.dfs(root.right, hashmap, idx+1, idy-1)

        return hashmap



