# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        
        # Brute force solution
        # edge case
        if not lists:
            return 
        stack = []
        for i in lists:
            while i:
                stack.append(i.val)
                i = i.next
        stack = sorted(stack)
        res = ListNode(-1)
        prev = res
        while stack:
            prev.next = ListNode(stack.pop(0))
            prev = prev.next            

        return res.next