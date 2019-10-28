class Solution:
    def findWords(self, words):
        
        keys = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        values = 1
        row = dict().fromkeys(keys, values)
        
        keys = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        values = 2
        row.update(dict().fromkeys(keys, values)) 
               
        keys = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        values = 3
        row.update(dict().fromkeys(keys, values)) 
        
        res = []
        for word in words:
            
            # check if all is the same number!!

            if len(set(row[c.lower()] for c in word)) == 1:
            
                res.append(word)
                
        return res


        


    