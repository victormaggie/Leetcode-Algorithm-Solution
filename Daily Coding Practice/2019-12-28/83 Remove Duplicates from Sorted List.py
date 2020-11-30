class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return
        
        dummy = ListNode(None)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

# time complexity o(N)
# space complexity o(1)

