# Author: Josh Thieme
# Date Created: Dec 1, 2021


class List:
    """This is creating the list class"""
    class Node:
        """This is creating the Node class"""
        def __init__(self, data):
            """Set up the variables that we will need for the nodes"""
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        """Set up the head and tail of the list"""
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """This is to insert a node into the list"""
        new_node = List.Node(value)

        # If the list is empty
        if self.head == None:
            # then create the head and tail to the new node
            self.head = new_node
            self.tail = new_node

        # if the list is not empty, then write the code that
        # would connect the head to the rest of the list
        else:
            new_node.next = self.head # this connects the new node to the previous head
            self.head.prev = new_node # this connects the previous head to the new node
            self.head = new_node # this updates the head to the new node
        

    def insert_tail(self, value):
        new_node = List.Node(value)

        # write your code here
        

    def insert_track(self, value, new_value):
        """This is to insert a node anywhere in the list"""
        
        pass
        # write your code here
    
    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list
    
    def __str__(self):
        """
        Return a string of the linked list.
        """
        output = "list["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

# Scenario:
# For this first test, you will need to insert the 4th track for a train
# to safely pass through town. The first 3 are already done for you.

# Write the code in the insert_tail function, then come back and create the 
# tail variable and insert it to the link using the function that you wrote.

track_01 = '##01##'
track_02 = '##02##'
track_03 = '##03##'
track_04 = '##04##'
tail = '##TAIL##'

print("\n=========== PROBLEM 1 TESTS ===========")
link = List()
link.insert_tail(tail)
link.insert_head(track_03)
link.insert_head(track_02)
link.insert_head(track_01)
print(link) # Expected outcome: list[##01##, ##02##, ##03##, ##04##, ##TAIL##]

print("\n=========== PROBLEM 2 TESTS ===========")
# Scenario:
# For this excersise, you will need to write the insert_track function
# then come back and implement what you wrote, calling that function.
link = List()
link.insert_tail(tail)
link.insert_head(track_03)
link.insert_head(track_02)
link.insert_head(track_01)
print(link) # Expected outcome: list[##01##, ##02##, ##03##, ##04##, ##TAIL##]

# Feel free to write your own remove() and / or remove_after() functions
# then implement them here