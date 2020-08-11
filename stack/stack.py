"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if self.__len__() == 0:
            return None
        else:
            popValue = self.storage[self.__len__()-1]
            self.storage.pop()
            return popValue


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    def get_value(self):
        return self.value
    def get_next_node(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def update_value(self, value):
        self.value = value

class LinkedStack:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        if self.head is None and self.tail is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        elif self.head != None and self.tail != None:
            new_node = Node(value)
            self.tail.set_next(new_node)
            self.tail = new_node
        else:
            return 'LinkedStack error'
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return 'Linked Stack is already empty!'
        elif self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return f'Removed the only node in the linked stack with a value of {val}.'
        elif self.head != None and self.head != self.tail:
            current = self.head
            while current.get_next_node() != self.tail:
                current = current.get_next_node()
            self.tail = current
            self.tail.set_next(None)
        else:
            return 'LinkedStack error'


ls = LinkedStack()

ls.add_to_tail(7)

ls.add_to_tail(2)

ls.remove_tail()

ls.add_to_tail(17)

print(f'LinkedStack Head: {ls.head.get_value()}')
print(f'LinkedStack Tail: {ls.tail.get_value()}')