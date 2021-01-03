
# Maximum Units On a Truck

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        
        stack = []
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        ans = 0
        
        for box, val in boxTypes:
            
            if truckSize >= box:
                ans += box * val
                truckSize -= box
            else:
                ans += truckSize * val
                break
        return ans

# o(nlogn) solution here!