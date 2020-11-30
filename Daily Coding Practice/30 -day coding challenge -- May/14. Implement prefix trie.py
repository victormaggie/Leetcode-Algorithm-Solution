class Node(object):
    def __init__(self):
        # This is the smart way to store and initiate the node
        self.children = collections.defaultdict(Node)
        self.isword = False

class Trie:
    def __init__(self):
        
        