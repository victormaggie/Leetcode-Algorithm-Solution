class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word):
        
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]      
        node['$'] = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node: return False
            node = node[char]
            if not node: return False
        
        return '$' in node
    
    def startsWith(self, word):
        node = self.root
        for char in word:
            if char not in node: return False
            node = node[char]
            if not node: return False
        
        return True