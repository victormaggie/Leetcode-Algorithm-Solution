
# merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        if not l1 and not l2: return None
        
        head = ListNode(0)
        curr = head
        while l1 or l2:
            
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
            
            if val1 > val2:
                head.val = val2
                l2 = l2.next
            else:
                head.val = val1
                l1 = l1.next
            
            if not l1 and not l2: break
            
            node = ListNode()
            head.next = node
            head = node
     
        return curr

# o(n) complexity

# we can only do the pointer manipulation here


class Solution:
    
    def mergeTwoLists(self, l1, l2):
        
        if not l1 or not l2: return None
        
        head = ListNode(0)
        curr = head
        while l1 or l2:
            
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
            
            if val1 > val2:
                head.next = l2
                head = head.next
                l2 = l2.next
            else:
                head.next = l1
                head = head.next
                l1 = l1.next
            
            if not l1 and not l2: break
        
        return curr.next

# o(n) time complexity
# o(1) space complexity
                
                
                
                
                
                
                
                