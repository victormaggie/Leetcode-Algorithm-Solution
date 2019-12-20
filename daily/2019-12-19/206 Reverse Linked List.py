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

            curr.next, prev, curr = prev, curr, curr.next

        return prev