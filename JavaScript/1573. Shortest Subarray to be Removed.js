class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        last = 0
        res = float('inf')
        i = 0
        count = collections.Counter(arr)
        front = 0
        while i < len(arr):
            stack = []
            
            if arr[i] >= last:
                last = arr[i]
                i += 1
            
            elif i - 1 >= 0 and count[arr[i-1]] > 1:
                front = i

            
            else:
                while i < len(arr) and arr[i] < last:
                    stack.append(arr[i])
                    i += 1
                
                if i < len(arr):
                    last = arr[i]
                res = min(res, len(stack))
        
        if res == float('inf'): return 0
        return res