Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        # define 3 node

        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


