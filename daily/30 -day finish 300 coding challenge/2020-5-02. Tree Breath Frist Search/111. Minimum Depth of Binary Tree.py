class Solution:
    def minDepth(self, root):
        if not queue: return 0
        queue = collections.deque()
        queue.append(root)
        cnt = 0
        while queue:
            max_len = len(queue)
            cnt += 1
            for _ in range(max_len):
                node = queue.popleft()
                if not node.left and not node.right:
                    return cnt
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

# time complexity o(h)
# space complexity o(n)

