import collections

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()
    
    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):

        if key not in self.cache:
            self.cache[key] = value
        self.cache.move_to_end(key)

        # update the self.cache matrix
        self.cache[key] == value

        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

# time complexity o(1)
# space complexity o(n)

# Implement LRU Cache from scratch

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
    
    def reset(self, key, val):
        self.key = key
        self.val = val

class LRUCache2(object):
    def __init__(self, capacity):
        self.key_to_idx = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.key_to_idx:
            return -1
        node = self.key_to_idx[key]

        self.move_to_end(node)
        return node.val
    
    def put(self, key, val):
        if key in self.key_to_idx:
            node_to_modify = self.key_to_idx[key]
            node_to_modify.val = val
            # put in the front of the hash
            self.get(key)
        
        elif len(self.key_to_idx) < self.capacity:
            new_node = Node(key, val)
            self.key_to_idx[key] = new_node

            if self.tail is None and self.head is None:
                self.tail = new_node
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        else:
            key_remove = self.tail.key
            del self.key_to_idx[key_remove]
            self.tail.reset(key, val)
            self.key_to_idx[key] = self.tail
            self.move_to_end(self.key_to_idx[key])
            
    
    def move_to_end(self, node):
        if node == self.head:
            return 
        
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            # delete the middle element
            node.next.prev = node.prev
            node.prev.next = node.next

        # put the element in the front
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node


