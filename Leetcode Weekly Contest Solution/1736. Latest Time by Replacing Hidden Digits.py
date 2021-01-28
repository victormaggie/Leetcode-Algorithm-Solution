
class Solution:
    
    def maximumTime(self, time):
        
        def check(tik, time):
            for char1, char2 in zip(tik, time):
                
                if char2 == '?' or char1 == char2: continue
                return False
            
            return True
            
            
        for i in range(23, -1, -1):
            for j in range(59, -1, -1):
                
                tik = str(i).zfill(2) + ':' + str(j).zfill(2)
                if check(tik, time): return tik
                
        return ''

# time complexity 23 * 60 * 5                