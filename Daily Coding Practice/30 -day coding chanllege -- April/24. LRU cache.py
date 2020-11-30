from typing import List
class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def reset(self, key, val):
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity):
        self.dict = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
    
    def get(self, key: int):
        if key in self.dict: 
            node = self.dict[key]
            self.move_to_head(node)
            return node.val
        else: return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.get(key)
        # if not in the the self.dict
        # we need increase the capacity of the hashmap
        elif len(self.dict) < self.capacity:
            new_node = TreeNode(key, value)
            # store to dictionary
            self.dict[key] = new_node
            # set as head
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        else:
            key_remove = self.tail.key
            del self.dict[key_remove]
            self.tail.reset(key, val)
            self.dict[key] = self.tail
            self.move_to_head(self.dict[key])

    def move_to_head(self, node):
        # 1. is head --> return
        if node == self.head: return 
        # 2. is tail --> 
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None

        # 3. is in between -->
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        # set the element in the front
        self.head.prev = node
        node.next = self.head
        node.prev = None
        # new head
        self.head = node

