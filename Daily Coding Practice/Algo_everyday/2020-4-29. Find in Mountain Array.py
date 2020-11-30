# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target, Mountain_arr):
        N = Mountain_arr.length()
        left, right = 0, N - 1
        
        
        # No. 1 --> find the peak value in the arr
        peak = 0

        ## here find the peak value has a bug !! 
        while left < right:
            mid = left + (right - left)//2
            if Mountain_arr.get(mid) < Mountain_arr.get(mid + 1):
                left = peak = mid + 1
            else:
                right = mid
            # only use the clibing algorithm if we use binary search
            # there is a bug shit !!
            # if mid - 1 >= 0 and mid + 1 < N and mid_val > Mountain_arr.get(mid - 1) and mid_val > Mountain_arr.get(mid + 1):
            #     peak = mid
            #     break
            # elif mid - 1 >= 0 and mid_val > Mountain_arr.get(mid - 1):
            #     left = mid + 1
            # elif mid + 1 < N and mid_val > Mountain_arr.get(mid + 1):
            #     right = mid - 1
            
        res = min(self.search_inc(Mountain_arr, 0, peak, target), self.search_dec(Mountain_arr, peak, N, target))

        if res == float('inf'):
            return -1
        return res
        # No.2 ---> find the split the search region
    def search_inc(self, Mountain_arr, left, right, target):
        
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = Mountain_arr.get(mid)

            if mid_val == target:
                return mid
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1
        return float('inf')
    
    def search_dec(self, Mountain_arr, left, right, target):
        while left <= right:
            mid = left + (right - left) //2 
            mid_val = Mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1
        return float('inf')
                
            