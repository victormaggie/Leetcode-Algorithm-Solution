class Solution:
    def __init__(self):
        """
        initialize the data structure here
        """
        self.stack = []
    
    def push(self, x):
        if not self.stack: self.stack.append((x, x))
        else: self.stack.append((x, min(x, self.stack[-1][1])))
    
    def pop(self):
        if self.stack: return self.stack.pop()[1]
        else: return
    
    def top(self):
        if self.stack: return self.stack[-1][0]
    
    def getMin(self): 
        if self.stack: return self.stack[-1][1]

# time complexity o(1)
# space complexity o(N)

