# we use the trie structure
import collections
class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word):

        current = self.root
        for w in word:
            current = current.children[w]
        
        current.isword = True
    
    def search(self, word):

        return self.match(word, 0, self.root)
    
    def match(self, word, index, root):
        if root == None:
            return False
        if index == len(word):
            return root.isword
        if word[index] != '.':
            return root != None and self.match(word, index +1, root.children.get(word[index]))
        else:
            for child in root.children.values():
                if self.match(word, index +1, child):
                    return True
        
        return False
        