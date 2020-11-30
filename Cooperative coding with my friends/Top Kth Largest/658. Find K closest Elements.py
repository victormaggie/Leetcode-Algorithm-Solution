class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        index = self.binary_search(arr, x)
        
        left = max(0, index - k)
        right = min(index + k, len(arr)-1)
        
        result = []
        for i in range(left, right+1):
            
            if len(result) < k:
                heappush(result, (-abs(x - arr[i]), -arr[i]))
                continue
            heappushpop(result, (-abs(x - arr[i]), -arr[i]))
        
        ans = []
        for i in result:
            ans.append(-i[1])
        return sorted(ans)
        
    
    def binary_search(self, arr, target):
        # return the index 
        left, right = 0, len(arr)-1
        
        while left <= right:
            
            mid = left + (right - left) //2 
            
            if arr[mid] == target: 
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


# use the binary search to find the index
# use heap to nlogk
