class Solution:
    def reverse_every_k_elements(head, k):
        if k <= 1 or not head: return head
        curr, prev = head, None
        while True:
            last_element_of_previous_part = prev
            last_element_of_sub_list = curr
            temp = None
            i = 0
            # reverse the linked list
            while curr and i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            
            # connect with the previous part
            if last_element_of_previous_part:
                last_element_of_previous_part.next = prev
            else: head = prev

            # connect with the next part
            last_element_of_sub_list.next = curr

            # if curr is None, we ALREADY finished the reverse then return 
            if not curr: break
            previous = last_element_of_sub_list
        return head

# this is pretty smart questions, split and join! nice
# time complexity o(N)
# space complexity o(1)

