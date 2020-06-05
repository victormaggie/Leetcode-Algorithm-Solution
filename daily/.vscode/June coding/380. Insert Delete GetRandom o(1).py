class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
    
    def insert(self, val:int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_element, idx = self.list[-1], self.dict[val]
        self.list[idx], self.dict[last_element] = last_element, idx
        # delete the value

        del self.dict[val]
        self.list.pop()
        return True
    
    def getRandom(self)->int:
        return random.choice(self.list)

# time complexity o(1)
# space complexity o(n)

