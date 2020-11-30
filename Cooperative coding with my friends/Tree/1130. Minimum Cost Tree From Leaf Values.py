class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0

        while len(arr) > 1:
            min_val = min(arr)
            idx = arr.index(min_val)

            if idx > 0 and idx < len(arr)-1:
                left_val, right_val = arr[idx-1], arr[idx+1]
            
            elif idx == 0:
                left_val, right_val = 16, arr[idx+1]
            
            elif idx == len(arr) - 1:
                left_val, right_val = arr[idx-1], 16
            
            res += min(min_val * left_val, min_val * right_val)

            arr.remove(min_val)
        
        return res

