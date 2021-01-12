
# a list of sorted array!

# the overall algorithm is to use Heap sort solution!

# LC 23

# This question need be focus on the difference of Python 2 and Python 3

def mergeKLists(lists):

    if not lists or not lists[0]: return None
    
    heap = []
    
    head = ListNode(0)
    curr = head
    
    for arr in lists:
        heapq.heappush(heap, (-arr.val, arr))
    
    while heap:
        
        (val, node) = heapq.heappop(heap)
        
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (-node.next.val, node.next))
    
    return head.next
    

# python 3 solution
def mergeKLists(lists):
    
    head = ListNode(0)
    curr = head
    
    if not lists: return 
    
    heap = []
    
    for i , link in enumerate(lists):
        if link: 
            heapq.heappush(heap, (link.val, i , link))
    
    # KlogK
    
    while heap:
    # o(n)
        (value, i, node) = heapq.heappop(heap)
        
        curr.next = node
        curr = curr.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, 500+i, node.next))
            # log(K)
    
    return head.next
    
   # O(nlogK) time complexity
   # o(K) space complexity
   
# python 2 can compare the object
# python 3 cannot compare ListNode object, so there will have fault
