class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution(object):
    def sortList(self, head):
        # brute force solution

        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        stack = sorted(stack)
        res = ListNode(-1)
        res = res
        for i in stack:
            prev.next = ListNode(i)
            prev = prev.next
        return res.next


# need check another solution like heapq-->
