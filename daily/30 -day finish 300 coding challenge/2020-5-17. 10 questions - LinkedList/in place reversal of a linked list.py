from __future__ import print_function

class Node:
    def __init__(self, val, next=Node):
        self.val = Value 
        self.next = next 
    
    def reverse_sub_list(head, p, q):
        # edge case
        if p == q:
            return head

        curr, pre = head, None
        i = 0
        while curr and i < p-1:
            pre = curr
            curr = curr.next
            i += 1
        
        # we split the Linked List into 3 parts
        # before p
        # between p and q
        # after q
        last_node_of_first_part = prev
        last_node_of_sub_list = curr
        temp = None
        # reverse the node in the string
        i = 0
        while curr and i < q - p +1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        # connect with the first part
        if last_node_of_first_part:
            last_node_of_first_part.next = prev
        # here is pretty smart, when p == 1, then head = prev
        else: head = prev
        # connect with the last part
        last_node_of_sub_list.next = curr
        return head
