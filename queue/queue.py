"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) >= 1:
            val = self.storage[0]
            self.storage.pop(0)
            return val
        else:
            return None


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
    

class LinkedQueue:
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
            return 'LinkedQueue error'
    def remove_head(self):
        if self.head != None and self.head.get_next_node() != None:
            val = self.head.get_value()
            self.head = self.head.get_next_node()
            return val
        elif self.head != None and self.head.get_next_node() == None:
            val = self.head.get_value()
            self.head = None
            return val
        else:
            return None


lq = LinkedQueue()

lq.add_to_tail(7)

lq.add_to_tail(2)

lq.remove_head()

lq.add_to_tail(17)

print(f'LinkedQueue Head: {lq.head.get_value()}')
print(f'LinkedQueue Tail: {lq.tail.get_value()}')