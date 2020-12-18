
class Solution:
	def balancedStringSplit(self, s):
		stack = []
		count_l, count_r = 0, 0
		temp = ''
		i = 0
		
		while i < len(s):
			if s[i] == 'R':
				count_r += 1
			
			else:
				count_l += 1
			
			temp += s[i]
			i += 1
			
			if count_l == count_r:
				stack.append(temp)
				temp = ''
			
		return len(stack)


class Solution:
    def balancedStringSplit(self, s):
        ans = 0
        count_l, count_r = 0, 0
        
        while i < len(s):
            
            if s[i] == 'R':
                count_r += 1
            
            else:
                count_l += 1
            
            if count_l == count_r:
                ans += 1
            
            i += 1
        return ans

# o(n) greedy solution, this question is a bit confusion.