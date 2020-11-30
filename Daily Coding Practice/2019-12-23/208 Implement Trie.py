# implement trie tree
# we use the method of collections.defaultdict(int)

import collections
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie(object):
    # initialization
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True
    
    def search(self, word):
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False      
        return current.isword

    def startWith(self, prefix):
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True

    
