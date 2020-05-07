class Solution:
    def isCousins(self, root, x, y):
        if not root: return
        queue = collections.deque()
        queue.append((root, None))
        while queue:
            max_len = len(queue)
            count = 0
            father = None
            for i in range(0, max_len):
                node, new_father = queue.popleft()
                if node.val == x or node.val == y:
                    count += 1
                    if father != None: father = (new_father != father)
                    else: father = new_father
                if node.left: queue.append((node.left, node))
                if node.right: queue.append((node.right, node))
            
            if father and count == 2: return True
            if father: return False
        return False

# bsf solution
# time complexity o(N)
# space complexity o(N)
