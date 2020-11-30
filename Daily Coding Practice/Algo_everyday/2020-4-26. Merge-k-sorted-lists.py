class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    

class Solution(object):
    def mergeKLists(self, lists):
        heap = []
        for i in list:
            if i: heapq.heappush(heap, (i.val, i))

        # another simplify syntax
        [heapq.heappush(heap, (i.val, i)) for i in lists if i]

        res = ListNode(None)
        move = res

        while heap:
            val, node = heapq.heappop(heap)
            new_node = ListNode(val)
            move.next = new_node
            move = move.next
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        
        return res.next

# time complexity o(Nlogk)
# space complexity o(N)