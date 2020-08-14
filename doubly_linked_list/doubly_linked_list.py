"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head == None:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head
        else:
            new_node = ListNode(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
            return self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None:
            return None
        elif self.length >= 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            val = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return val



            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head == None: 
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head
        else:
            new_node = ListNode(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            return self.tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None:
            return None
        elif self.length >= 1:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        else:
            val = self.head.value
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #1.set input node.prev.next to none and node.next.prev to each other (if they exist)
        if node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev
            #2.set input node's prev to none
            node.prev = None
            #3.set input node's next to self.head and current head's prev to input node
            node.next = self.head
            self.head.prev = node
            #4.set self.head to input node
            self.head = node
        elif node == self.head:
            return 'That node is already the head!'
        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev #extra step if the node is the tail
            #2.set input node's prev to none
            node.prev = None
            #3.set input node's next to self.head and current head's prev to input node
            node.next = self.head
            self.head.prev = node
            #4.set self.head to input node
            self.head = node
        else:
            return 'Node does not have a next or prev and is not the head or tail of this doubly list. What are you doing?????'

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #1.set input node.prev.next to none and node.next.prev to each other (if they exist)
        if node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev
            #2.set input node's next to none
            node.next = None
            #3.set input node's prev to self.tail and current tail's next to input node
            node.prev = self.tail
            self.tail.next = node
            #4.set self.tail to input node
            self.tail = node
        elif node == self.tail:
            return 'That node is already the tail!'
        elif node == self.head:
            node.next.prev = None
            self.head = node.next #extra step if the node is the head
            #2.set input node's next to none
            node.prev = None
            #3.set input node's prev to self.tail and current tail's next to input node
            node.prev = self.tail
            self.tail.next = node
            #4.set self.tail to input node
            self.tail = node
        else:
            return 'Node does not have a next or prev and is not the head or tail of this doubly list. What are you doing?????'

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #set node.next.prev to noded.prev and node.prev.next to node.next (if exists)
        if node.next != None and node.prev != None:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1
            #delete node - python does this automatically?
        #if the node was a head or a tail set the new head or tail
        elif node == self.head:
            if node.next == None:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.head = node.next
                node.next.prev = None
                self.length -= 1
        elif node == self.tail:
            if node.prev == None:
                self.head = None
                self.tail = None
                self.length -= 1
            else:
                self.tail = node.prev
                node.prev.next = None
                self.length -= 1
        else:
            return '???'

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        currNode = self.head
        highestVal = 0
        for i in range(self.length):
            if currNode.value > highestVal:
                highestVal = currNode.value
            currNode = currNode.next
        return highestVal

# dll = DoublyLinkedList(ListNode(5))

# dll.add_to_head(8)

# dll.remove_from_head()

# dll.add_to_tail(7)

# dll.add_to_tail(4)

# #dll.remove_from_tail()

# dll.move_to_front(dll.head.next)

# print(f'DoublyLinkedList Head: {dll.head.value}')
# print(f'DoublyLinkedList Head.Next: {dll.head.next.value}')
# print(f'DoublyLinkedList Tail: {dll.tail.value}')
# print(f'DoublyLinkedList Length: {dll.length}')