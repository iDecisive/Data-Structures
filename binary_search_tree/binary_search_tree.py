"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree ----- what about accounting for dupes?
    def insert(self, value):
        #check if value is less than this node's value
        if value < self.value:
            #does current node have a left child? If so, try the same method on it instead
            if self.left != None:
                self.left.insert(value)
            #otherwise (if there is space there), set self.left to the new node
            else:
                self.left = BSTNode(value)
        #now, since the value is greater than or equal to the current node's we'll look to the right
        else:
            if self.right != None:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #Does the current node == target?
        if target == self.value:
            return True
        #else, check if target is greater or less than the target and use recurrsion appropriately
        elif target > self.value and self.right != None:
            return self.right.contains(target)
        elif target < self.value and self.left != None:
            return self.left.contains(target)
        #else, it's not here buddy
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right != None:
            self.right.for_each(fn)
        if self.left != None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left != None:
            self.left.in_order_print()
        print(self.value)
        if self.right != None:
            self.right.in_order_print()


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):

        from collections import deque

        q = deque()
        q.append(self)
        
        while len(q) > 0:
            current_node = q.popleft()

            #check if node has children
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        print(self.value)
        if self.left != None:
            self.left.dft_print()
        if self.right != None:
            self.right.dft_print()

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self):
    #     pass

    # Print Post-order recursive DFT
    # def post_order_dft(self):
    #     pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
