Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

Class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Brute force solution
        """
        k = 0
        if not head:
            return
        cur = head
        while cur:
            cur = cur.next
            k += 1
            
        if k < n:
            return
        
        num = k - n + 1
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        
        while curr.next:
            num -= 1
            if num == 0:
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next

# solution 2 use heapq

