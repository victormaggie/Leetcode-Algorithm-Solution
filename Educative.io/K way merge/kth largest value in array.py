
# merge two sorted array find the Kth smallest number

def find_kth_smallest(lists, k):
    
    if not nums: return -1
    
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
            continue
        
        heapq.heappushpop(heap, num)
    
    return heap[0]

# nlogK solution heap
