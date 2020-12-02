
class Solution:
    def sortList(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        stack.sort(reverse=True)

        node = ListNode(0)
        front = node
        while stack:
            value = stack.pop()
            node.next = ListNode(value)
            node = node.next

        return front.next

# Time complexity o(nlogn)
# space complexity o(n)
