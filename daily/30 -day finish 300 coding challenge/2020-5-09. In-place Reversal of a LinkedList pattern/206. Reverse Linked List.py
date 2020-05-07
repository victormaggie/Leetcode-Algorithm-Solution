class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while head:
            curr = head.next
            head.next = prev
            prev = head
            head = curr
        return prev

# time complexity o(N)
# space complexity o(1)


class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

# time complexity o(N)
# space complexity o(1)


