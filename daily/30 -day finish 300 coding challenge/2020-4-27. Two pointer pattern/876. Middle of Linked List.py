class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            return slow.next
        return slow
# time complexity o(n)
# space complexity o(1)


# when the fast pointer reach the end, this is the end of the calculation
class Solution:
    def middleNode(self, head):
        fast = slow =head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

# time complexity o(n)
# space complexity o(1)

