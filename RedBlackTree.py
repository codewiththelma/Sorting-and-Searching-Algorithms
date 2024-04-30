"""
Author: gauri
Purpose: This file implemented creation of a Red Black Tree and
insertion operation in the three.

In a nutshell, there are two classes: NewNode that creates an instance of new node to be added in the tree
and the class RedBlackTree which  contains methods for creating a new Node, insertion and maintaining the balance in the tree.
"""

class NewNode:
    def __init__(self, value, color='red'): # Initializes a new Node with given value and color red by default
        self.value = value # The data part of each node
        self.left = None #  Left child of this node
        self.right = None # Right child of this node
        self.parent = None # Parent fo this node
        self.color = color # color of this node which is "red" by default

class RedBlackTree:
    def __init__(self): # Initializes a new tree with a root node
        self.root = None

    def insert(self, value): #  Insert a new node into the tree
        new_node = NewNode(value) 
        if self.root is None: #  If tree is empty, make root as new node
            self.root = new_node 
            self.root.color = 'black' #  change the color to black as root is always black
            return

        temp = self.root #  Start from root and search for the right position
        while temp: # search for the right position according to the binary tree logic  
            parent = temp 
            if value < temp.value: #  Go to left subtree
                temp = temp.left
            else: #  Go to right subtree
                temp = temp.right #  value is greater than current node so go to right

        new_node.parent = parent #  Set the parent of new node
        if value < parent.value:  #   check if the value is less than the parent
            parent.left = new_node # assign the new node as the left child of the parent
        else: 
            parent.right = new_node # assign the new node as the right child of the parent

        self._fix_insert(new_node) # call function to check the balance in the tree

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':  #  Check if we need to fix violation
            if node.parent == node.parent.parent.left: #  Node’s parent is left child of its parent (grandparent)
                uncle = node.parent.parent.right # then the uncle is the right child of grandparent (assign it)
                if uncle and uncle.color == 'red': # if the color is red
                    node.parent.color = 'black' # change the color of parent and uncle to black
                    uncle.color = 'black'
                    node.parent.parent.color = 'red' #   Change the color of grand parent to red
                    node = node.parent.parent # assign  the parent of parent to new node
                else:
                    if node == node.parent.right: #  if node is on the right side of its parent
                        node = node.parent # get the parent node to perform rotation
                        self._left_rotate(node) # perform left rotation
                    node.parent.color = 'black' # change the color of parent to black
                    node.parent.parent.color = 'red' # change the color of grandparent to red
                    self._right_rotate(node.parent.parent) # perform right rotate  on the grandparent
            else:
                uncle = node.parent.parent.left # find the uncle of the node
                if uncle and uncle.color == 'red': # if the uncle is red 
                    node.parent.color = 'black' # change the color of parent an grandparent to black
                    uncle.color = 'black'
                    node.parent.parent.color = 'red' # change the color of grandparent to red
                    node = node.parent.parent # assign  the parent of parent to new node
                else:
                    if node == node.parent.left: # If node is on the left side of its parent then make it right child of its parent and vice
                        node = node.parent # get the parent node to perform rotation
                        self._right_rotate(node) # perform right rotation
                    node.parent.color = 'black' # change the color of parent to black
                    node.parent.parent.color = 'red' # change the color of grandparent to red
                    self._left_rotate(node.parent.parent)  # perform left rotation
        self.root.color = 'black' # make sure that root is black

    def _left_rotate(self, node): #  Function for performing Left-Rotate
        right_child = node.right #  take the right child of the input node
        node.right = right_child.left # set the left subtree of the right child as the right subtree of the input node
        if right_child.left: #   If there is a left subtree then perform two steps down
            right_child.left.parent = node #  set the parent of the left child of the right child to be the input node
        right_child.parent = node.parent #  set the parent of right child to be same as parent of input node
        if not node.parent: 
            self.root = right_child #   if no parent exists then make right child as new root
        elif node == node.parent.left: #    if the input node is the left child of its parent
            node.parent.left = right_child #      set the left child of parent as right child of right child
        else: #  node must be node.parent.right
            node.parent.right = right_child 
        right_child.left = node #  Set the left child of right child to be the input node
        node.parent = right_child #  Set the parent of input node to be the right child

    def _right_rotate(self, node): #  Function for performing Right-Rotate
        left_child = node.left #      take the left child of the input node
        node.left = left_child.right #    Perform one step up from left child
        if left_child.right: # If there is a right subtree in left child then set its parent as the input node
            left_child.right.parent = node #  set the parent of the newly added node to be the input node
        left_child.parent = node.parent #  Set the parent of left child to be same
        if not node.parent: #  If no parent exists then make left child as new root
            self.root = left_child
        elif node == node.parent.right: # If the input node is the right child of its parent
            node.parent.right = left_child # Make left child as the right child of parent
        else:
            node.parent.left = left_child # Make left child as the left child of parent
        left_child.right = node #   Set the right child of left child to be the input node
        node.parent = left_child #   Set the parent of input node to be the left child


    def print_tree(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, level): # Helper function to print tree in level order fashion
        if node is not None:
            self._print_tree_recursive(node.right, level + 1)
            print('   ' * level + str(node.value) + ' (' + node.color + ')')
            self._print_tree_recursive(node.left, level + 1)


 
# Example usage:
tree = RedBlackTree()
values = [7, 3, 18, 10, 22, 8, 11, 26]
for value in values:
    tree.insert(value)

# Print the Red-Black Tree
tree.print_tree()
