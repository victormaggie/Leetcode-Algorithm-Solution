class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        def getall(nests):
            for nest in nests:
                if nest.isInteger():
                    self.stack.append(nest.getInteger())
                else:
                    getall(nest.getList())
        getall(nestedList)
    def next(self):
        if hasNext(): return self.stack.pop(0)
    def hasNext(self):
        return len(self.stack)

# time complexity o(L+N)
# space complexity o(N)
