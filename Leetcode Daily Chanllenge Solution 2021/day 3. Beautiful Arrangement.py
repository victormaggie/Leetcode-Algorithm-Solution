
class Solution:
	def countArrangement(self, n):
		
		# number of permutation
        self.count = 0
        visited = set()
        
        def dfs(n, visited, temp):
            
            if len(temp) == n:
                self.count += 1
                return
            
            for i in range(1, n+1):
                
                if i not in visited and ((len(temp)+1) % i == 0 or (i % (len(temp) + 1) == 0)):
                    
                    temp.append(i)
                    visited.add(i)
                    dfs(n, visited, temp)
                    temp.pop()
                    visited.remove(i)
                
        dfs(n, visited, [])
        
        return self.count

# the value here o(n * 2 ^ n) solution

        