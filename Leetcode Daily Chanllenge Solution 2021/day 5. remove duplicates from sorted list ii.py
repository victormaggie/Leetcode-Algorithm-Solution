
# Remove Duplicates from Sorted List II

# This is a very tricky question !! 

class Solution:
    
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        
        while head and head.next:
            
            if head.val == head.next.val:
                if head.next and head.next.val == head.val:
                    head = head.next
                
                head = head.next
                curr.next = head
            
            else:
                curr = curr.next
                head = head.next

        return dummy.next

# o(n) solution 