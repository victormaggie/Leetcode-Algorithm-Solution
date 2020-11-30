# This question is really good!
# solve this use DFS 
# solve this question use BFS

class Node:
    def __init__(self, x, next, random):
        self.val = int(x)
        self.next = next
        self.random = random

def class Solution:
    def __init__(self):
        self.seen = {}
    
    def copyRandomList(self, head):
        if not head: return None

        if head in self.seen:
            return self.seen[head]
        # create a new node
        node = Node(head.val, None, None)

        # create a new node
        self.seen[head] = node
        # recursion
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node

# time complexity o(n)
# space complexity o(n)

        