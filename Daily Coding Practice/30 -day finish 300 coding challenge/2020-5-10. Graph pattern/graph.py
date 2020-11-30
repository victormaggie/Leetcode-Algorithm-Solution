# from LinkedList import LinkedList
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
        
    def add_edge(self, source, destination):
        # Function to add an edge from source to destination
        if (source < self.vertices and destination < self.vertices):
            self.array[source].insert_at_head(destination)
    
    def print_graph(self):
        print(">> Adjacency List of Directed Graph <<")
        # print the vertices
        for i in range(self.vertices):
            print('|', i, end= '|=>')
            temp = self.array[i].get_head()
            while (temp is not None):
                print("[", temp.data, end='] ->')
                temp = temp.next_element
            print('None')
