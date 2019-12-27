
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
        heapq.heapify(nums)

        [heapq.heappush(num, (list.val, list)) for list in lists if list]
        
        # iterate the heap 
        while nums:
            # pop the smallest Node value tuple
            curVal, curHead = heapq.heappop(nums)
            # pop the node
            move.next = curHead
            move = move.next
            curHead = curHead.next
            if curHead:
                heapq.heappush(nums, (curHead.val, curHead))

        return head.next

# time complexity o(nlog(k))

