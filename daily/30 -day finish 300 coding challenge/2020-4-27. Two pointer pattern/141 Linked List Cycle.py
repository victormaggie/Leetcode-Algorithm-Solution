class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head):
        if not head: return

        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
    
# time complexity o(N)
# space complexity o(1)



# give a cycle linked list find the length of the linked list

class solution:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head):
        if not head: return
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return self.find_length_cycle


    def find_length_cycle(self, fast):
        curr = fast
        count = 0

        while True:
            curr = curr.next
            count += 1
            if curr == fast:
                break
        return count
        

# time complexity o(N )
# space complexity o(1)

