
import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists):
        
        # dummy ListNode
        head = ListNode(-1)
        move = head
        nums = []
        # initialize the heap
        import heapq
        heapq.heapify(nums)

        for list in lists:
            # define a heapq 
            if list != None:
                heapq.heappush(nums, list)
        
        # iterate the heap 
        while (not nums):
            # pop the smallest Node
            curHead = heapq.heappop(nums)
            # pop the node
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                heapq.heappush(nums, (curHead.val, curHead))

        return head.next


