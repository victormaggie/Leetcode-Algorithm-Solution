
# abbreviation solution

class Solution:
    def generateAbbreviations(self, word):
        
        # recursion solution here
        
        res = []
        
        def dfs(word, abword, start, count, result):
            
            # stop condition
            if start == len(word):
                if count != 0: abword.append(str(count))
                result.append(''.join(abword))
            
            else:
                
                # continue abbreviation by incrementing the current abbreviation count
                dfs(word, list(abword), start+1, count+1, result)
                
                
                # restart abbreviation, append the current character to the string
                if count != 0: abword.append(str(count))
                
                # restart abbreviation after start
                newword = list(abword)
                newword.append(word[start])
                dfs(word, newword, start+1, 0, result)
        
        dfs(word, [], 0, 0, res)
        
        return res

# o(n * 2^n) solution
        