class FirstUnique:
    def __init__(self, nums):
        self.dict = {}
        self.stack = []
        for i in nums:
            self.dict[i] = self.dict.get(i, 0) + 1
        for i in self.dict:
            if self.dict[i] == 1:
                self.stack.append(i)
        #[self.stack.append(i) for i in self.dict if self.dict[i] == 1]
    
    def showFirstUnique(self):
        if self.stack:
            return self.stack[0]
        else:
            return -1
    
    def add(self, value):
        if value in self.dict and self.dict[value] > 1:
            self.dict[value] = self.dict.get(value) + 1
        elif value in self.stack:
            self.dict[value] = 2
            self.stack.remove(value)
        else:
            self.stack.append(value)

