# Hard question

class Solution:
    def numOfWays(self, n):
        a121, a123, mod = 6, 6,  10**9 +7
        for i in range(n-1):
            a121, a123 = a121 * 3 + a123 * 2 , a121 * 2 + a123 * 2
        return (a121 + a123) % mod

# easy
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for j in words:
                if i != j and (i in j):
                    res.append(i)
                    
        return list(set(res))

# o(n^2)
# o(1)

# medium

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        res = []
        permutation = [i for i in range(1, m+1)]
        
        for i in range(len(queries)):
            num = queries[i]
            position = permutation.index(num)
            res.append(position)
            permutation = [permutation[position]] + permutation[:position] + permutation[position+1:]
        
        return res
# medium 
class Solution:
    def entityParser(self, text: str) -> str:
        
        hash_map = {
            "&quot;" : (6, '"'),
            "&apos;" : (6, "'"),
            "&amp;" : (5, '&'),
            "&gt;" : (4, '>'),
            "&lt;" : (4,  '<'),
            '&frasl;' : (7, '/')
        }
        
        Flag = True
        
        for i in hash_map:
            length, quote = hash_map[i]
            Flag = text.find(i)
            while Flag != -1:
                text = text[:Flag] + quote + text[Flag+length:]
                Flag = text.find(i)
                
        return text

    # optimization
    def entityParse(self, text):
        if not text:
            return 
        hash_map = {
            "&quot;" : (6, '"'),
            "&apos;" : (6, "'"),
            "&amp;" : (5, '&'),
            "&gt;" : (4, '>'),
            "&lt;" : (4,  '<'),
            '&frasl;' : (7, '/')
        }

        for k, v in hash_map.items():
            text = v.join(text.split(k))
        return text
