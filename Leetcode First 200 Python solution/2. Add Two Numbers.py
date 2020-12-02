class Solution:
    def addTwoNumbers(self, l1, l2):
        res = ListNode(0)
        front = res
        carrier = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carrier
            res.next = ListNode(total_sum % 10)
            res = res.next
            carrier = total_sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carrier: res.next = ListNode(carrier)

        return front.next

# o(n) solution, this is pretty good one.