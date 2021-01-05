import collections

class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isWord = False


class Solution:
    # initialization
    def __init__(self):
        self.root = Node()
    
    # insert method
    def insert(self, word):
        # object reference here
        node = self.root
        for char in word:
            # add the key and move next!
            node = node.children[char]
        
        node.isWord = True
            
    # search method
    def search(self, word):
        
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node == None: return False
        
        return node.isWord
        
    # check start with
    def startsWith(self, word):
        
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node == None: return False
         
        return True
        