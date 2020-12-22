
# Decoded string, in this question, be aware of that
# char * n is o(n) copy

class Solution:
    
    def decodeAtIndex(self, S, K):
        stack = ''
        for char in S:
            
            if char.isalpha():
                stack += char
            
            if len(stack) >= K: return stack[K-1]
            
            if char.isnumeric():
                if len(stack) * int(char) >= K: return stack[K % len(stack)-1]
                stack = stack * int(char)
    
        return stack[K]

# this solution will ETL o(n ^ 2)



# more efficient solution

def Solution:
    def decodeAtIndex(self, S, K):
        size = 0
        
        for c in S:
            if c.isdigit():
                c *= int(c)
            
            else:
                c += 1
        
        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c
            
            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
        
        