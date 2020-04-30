# definition for single linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next: return True
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        copyreverse = self.reverse(slow)
        store = copyreverse
        while head and copyreverse:
            if head.val != copyreverse.val:
                return False
            head = head.next
            copyreverse = copyreverse.next
        self.reverse(store)
        if not head or not copyreverse:
            return True

    # reverse a linked list

    def reverse(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous

# time complexity o(N)
# space complexity o(1)

