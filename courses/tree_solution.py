# Author: Josh Thieme
# Date Created: December 2, 2021

class Tree:
    class Node:
        def __init__(self, data):
            """Initialize the nodes"""
            self.data = data
            self.left = None
            self.right = None
    def __init__(self):
        """Initialize the trees root"""
        self.root = None

    def insert_node(self, data):
        """Insert a node to the tree"""

        # If root is empty
        if self.root is None:
            # Initialize it to the tree's data
            self.root = Tree.Node(data)
        # Otherwise
        else:
            # Start at the root
            self.insert_tree_node(data, self.root)

    def insert_tree_node(self, data, node):
        """This will actually do the real 
        searching to insert a node to the tree"""
        
        # If the value is less than the previous, put it on the left!
        if data < node.data:
            # If the node is empty
            if node.left is None:
                # Then give it the new value
                node.left = Tree.Node(data)
            # Otherwise
            else:
                # Keep looking in a recursive manner.
                self.insert_tree_node(data, node.left)
        # If the value is the same
        elif data == node.data:
            # Get outta there! NO DUPLICATES!
            return
        # Otherwise find the value for the right side
        else:
            # IF there's an empty spot
            if node.right is None:
                # Then put the value there
                node.right = Tree.Node(data)
            # Otherwise
            else:
                # Keep looking for the right side
                self.insert_tree_node(data, node.right)

    def __iter__(self): 
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        This allows for the tree to search from
        the root going down to the leaves
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
    
    def __reversed__(self):
        """This allows for the tree to go backwards"""
        yield from self._backwards_tree_(self.root)

    def _backwards_tree_(self, node):
        """This is the real backwards traversal"""
        if node is not None:
            yield from self._backwards_tree_(node.right)
            yield node.data
            yield from self._backwards_tree_(node.left)


# Write the code for the insert_tree_node function.
# You will also have to put in the function a rule
# that will not allow for any duplicate values.
# This time, the insertion code is already done for you.
print("\n=========== PROBLEM 1 TESTS ===========")
tree = Tree()
tree.insert_node(15)
tree.insert_node(5)
tree.insert_node(20)
tree.insert_node(7)
# After implementing no duplicates rule,
# this next insert will have no effect on the tree.
tree.insert_node(7)  
tree.insert_node(4)
tree.insert_node(17)
tree.insert_node(25)

for x in tree:
    print(x)  # 4, 5, 7, 15, 17, 20, 25

print("\n=========== PROBLEM 2 TESTS ===========")
# You will need to write the code for the _backwards_tree_ function.
# Hint: It's easier than you think! Solve the small problem.
for x in reversed(tree):
    print(x)