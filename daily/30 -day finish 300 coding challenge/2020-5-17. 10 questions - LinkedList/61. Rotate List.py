class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not k or not head: return head
        curr, prev = head, None
        max_len = 0
        while curr:
            prev = curr
            curr = curr.next
            max_len += 1
        
        # connect the node --> generate a cycle
        prev.next = head
        # here I put the initialization point at the end!
        curr = prev.next

        # iterate k times still
        # nice ! this is correct and smart way to handle it
        i = 0
        while curr and i < (max_len - k % max_len):
            prev = curr
            curr = curr.next
            i += 1
        # finally break it down
        prev.next = None
        return curr

# time complexity o(n)
# space complexity o(1)

    def rotateRight(head, k):
        # check the boundary
        if not head or not head.next or k <= 0: return head
        # find the length and the last node of the list
        last_node = head
        list_length = 1
        while last_node.next:
            last_node = last_node.next
            list_length += 1
        
        # connect with head
        last_node.next = head
        k %= list_length
        skip_lenght = list_length - k
        # here put the initial point at the head
        last_node_of_rotated_list = head
        for i in range(skip_lenght - 1):
            last_node_of_rotated_list = last_node_of_rotated_list.next

        head = last_node_of_rotated_list.next
        last_node_of_rotated_list.next = None
        return head

