# implement LinkedList
from Node import Node

class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:
            return True
        else:
            return False
    
    def insert_at_head(self, dt):
        # constant time
        temp_node = Node(dt)
        if self.is_empty():
            self.head_node = temp_node
            return self.head_node
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node
    
    def insert_at_tail(self, dt):
        temp_node = Node(dt)
        if self.is_empty:
            self.head_node = temp_node
            return self.head_node
        # if it is not empty
        temp = self.get_head()
        while temp:
            temp = temp.next_element
        
        temp.next_element = temp_node
        return

    def length(self):
        curr = self.get_head()
        length = 0
        while curr:
            length += 1
            curr = curr.next_element
        return length
    
    def print_list(self):
        if (self.is_empty()):
            print("LIst is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end='->')
            temp = temp.next_element
        print(temp.data, "->None")
        return True

    def delete_at_head(self):
        first_element = self.get_head()
        if first_element:
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    # delete value here
    def delete(self, value):
        deleted = False
        if self.is_empty():
            return deleted
        
        current_node = self.get_head()
        previous_node = None
        if current_node.data == value:
            self.delete_at_head()
            deleted = True
            return deleted
        while current_node:
            if value is current_node.data:
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element
        return deleted
        
    def search(self, dt):
        if self.is_empty():
            print('List is Empty')
            return None
        temp = self.head_node
        while temp:
            if temp.data is dt:
                return temp
            temp = temp.next_element
        
    def remove_duplicates(self):
        if self.is_empty():
            return
        if self.get_head().next_element is None:
            return 

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node
            while inner_node:
                # are you kind o(n2) time complexity
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        inner_node = inner_node.next_element
                else:
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return
