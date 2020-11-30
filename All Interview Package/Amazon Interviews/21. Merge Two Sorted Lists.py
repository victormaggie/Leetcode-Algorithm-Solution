class Solution:
    def mergeTwoList(self, l1, l2):
        dummy = ListNode(0)
        head = dummy

        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        head.next = l1 if l1 else l2

        return dummy.next

# o(n) running time
# o(1) space complexity


