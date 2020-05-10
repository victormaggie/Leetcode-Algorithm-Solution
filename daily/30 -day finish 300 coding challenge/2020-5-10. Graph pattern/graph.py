class LinkedList:
    def __init__(self,):
        

class Graph:
    def __init__(self, vertices):
        # total number of vertices
        self.vertices = vertices
        # define a list which can hold multiple LinkedList
        self.array = []
        # create a new LinkedList for each vertex/index
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)
