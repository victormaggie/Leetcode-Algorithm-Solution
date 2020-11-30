class Solution:
    def reverseLinkedList(self, head, k):
        if not head or k <= 1: return head
        curr, prev = head, None
        while True:
            last_element_of_firts_part = prev
            last_element_of_sub_list = curr

            i = 0
            temp = None
            while curr and i < k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            
            # connect the first part and and sub list

            if last_element_of_firts_part: last_element_of_firts_part.next = prev
            else: head = prev

            # connect the sub list part to next part
            last_element_of_sub_list.next = curr

            ##############################################################  HOW TO CHECK THE BOUNDARY PART !!!!>????? ######
            leader = curr
            while leader:
                leader = leader.next
                i += 1
            if i < k: return head
            if not curr: break
            prev = last_element_of_sub_list
        return head

# OMFG ! how to handle this last part and check if its length == k !!
# this solution is not optimized !!


