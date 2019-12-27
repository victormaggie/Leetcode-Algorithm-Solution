class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            """
            curr.next = prev
            prev = curr
            curr = curr.next
            """
            # here update all the node simultaneously
            curr.next, prev, curr = prev, curr, curr.next

        return prev