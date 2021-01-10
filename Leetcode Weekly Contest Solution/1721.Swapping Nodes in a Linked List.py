
# 1721 Swapping Nodes in a Linked list

class Solution:
    
    def swapNodes(self, head):
        
        n = 0
        curr = head
        stack = []
        
        while head:
            stack.append(head.val)
            n += 1
            head = head.next
        
        stack[k-1], stack[n-k] = stack[n-k], stack[k-1]
        
        curr = ListNode(0)
        dummy = curr
        while stack:
            val = stack.pop(0)
            node = ListNode(val)
            curr.next = node
            curr = curr.next
        
        return dummy.next
        
    
    def swapNodes(self, head):
        ans = []
        current = head
        while current:
            ans.append(current)
            current = current.next
        
        ans[k-1].val, ans[len(ans) - k].val = ans[len(ans) - k].val, ans[k-1].val
        
        return head

# head!
