import collections

# define node class
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)    # define the dictionary for Hash
        self.isword = False                              # iscomplete check


class Trie(object):

    # constructor -> define root empty node
    def __init__(self):
        self.root = Node()
    
    # insert element 
    def insert(self, word):
        current = self.root
        for w in word:
            current = current.children[w]
        current.isword = True
    
    # traversal the word in the dictionary
    def search(self, word):
        current = self.root
        for w in word:
            current = current.children.get(w)
            if current == None:
                return False
        return current.isword    # check the final words
    
    def startsWith(self, prefix):
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True              # only need to return the final one
