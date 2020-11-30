class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head: return
        odd = head
        even = head.next
        evenhead = even
        while even.next and odd.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenhead
        return head

# Linkedlist we need take care of the left end and right end

# time complexity o(n)
# space complexity o(1)