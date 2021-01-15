# Merge Intervals
class Solution:
	
	def merge(self, intervals):
		
		intervals.sort()
        
		ans = [intervals[0]]
		
		for interv in intervals[1:]:
			
			if interv[0] > ans[-1][1]:
				ans.append(interv)
				continue
			
			up_interv = ans.pop()
			
			front_val = min(up_interv[0], interv[0])
			back_val = min(up_interv[1], interv[1])
			
			ans.append([front_val, back_val])
			
		return ans

# o(n) solution here!
# o(n) Time complexity solution here!

	