class ListNode:
    def __init__(self, val = 0, m, n):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, m, n):
        if m == n or not head: return head

        curr, prev = head, None

        # skip the first part
        i = 0 
        while curr and i < k-1:
            prev = curr
            curr = curr.next
            k += 1
        
        # split the linked list

        last_element_of_first_part = prev
        last_element_of_sub_list = curr

        # reverse the sublist
        i = 0
        while curr and i < n - m + 1:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        
        # connect the element together
        if last_element_of_first_part: last_element_of_first_part.next = prev
        else: head = prev

        # connect the final part
        last_element_of_first_part.next = curr
        return head

# time complexity o(n)
# space complexity o(1)


