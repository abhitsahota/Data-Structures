class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class SingleLL:
    def __init__(self):
        self.head = Node
        self.tail = Node

    def __str__(self):
        output = ''
        current_node = self.head # create a tracker node
        while current_node is not None: # loop till it's none
            output += f'{current_node.value} -> '
            current_node = current_node.next_node # update tracker node to next element
        return output

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value, None)
        if self.head is None and self.tail is None:
             self.head = new_node
             self.tail = new_node 
        else:
            new_node.next_node = self.head
            self.head = new_node

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.next_node:
            current_val = self.head
            self.head = None
            self.tail = None
            return current_val.value
        print('something back', self.head)
        current_val = self.head.value
        self.head = self.head.next_node
        return current_val

    # def get_max(self):
    #     pass     

    def contains(self, value):
        if self.head is None:
            return False
        current.node = self.head
        while current_node is not None:
            if current_node.value == value:
                return True
            current_node = current_node.next_node
        return False