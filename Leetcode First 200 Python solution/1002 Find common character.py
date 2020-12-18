class Solution:
	def commonChars(self, A):
		# find the common value here
        
        hashmap = collections.Counter(A[0])
        
        for a in A:
            # use the container intersection here
            hashmap &= collections.Counter(a)  
        
        return list(hashmap.elements())

# the o(n^2) solution
