class Solution:
    def detectCycle(self, head):
        if not head: return
        # calculate if we have cycle linked list
        k = self.catch_up(head)
        if k == False: return None

        fast = head
        slow = head
        while k:
            fast = fast.next
            k -= 1
        
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
    
    def num_cycle(self, head):
        cur = head.next
        count = 1
        while cur != head:
            cur = cur.next
            count += 1
        return count
    
    def catch_up(self, head):
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow =slow.next
            if fast == slow:
                return num_cycle(fast)
        return False

# time complexity o(N)
# space complexity o(1)

