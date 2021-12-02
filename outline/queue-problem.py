# Author: Josh Thieme
# Date Created: 22 Nov 2021

"""This is to practice the enqueue() and dequeue() functions.
Please do not share or copy this code to others."""
class Queue:
    """Keep order in a queue using a Python List"""
    def __init__(self):
        """Initializing the queue list"""
        self.queue = []

    def enqueue(self, letter):
        """Be able to add a letter to the end of the queue"""
        pass
        # write your answer here
    
    def dequeue(self):
        """Be able to remove a letter from the front of the queue"""
        if len(self.queue) <= 0:
            raise IndexError
        # write your answer here



# Test 1
# Objective: Enqueue a letter, then dequeue that letter.
# Expected Result: Should display: A

print('Test 1')
queue = Queue()
queue.enqueue('A')
print(queue.dequeue())

# Test 2
# Objective: Enqueue multiple letters, and dequeue the first four letters.
# Expected Result: Should display: A B C D
print('*********************')
print('Test 2')
queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')
queue.enqueue('F')
queue.enqueue('G')
queue.enqueue('H')
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

# Test 3
# Obective: What happens if the queue is empty?
# Expected Result: Should display some exception

print('*********************')
print('Test 3')
queue = Queue()

try:
    queue.enqueue()
    print("Uh Oh! That's not good!")
except:
    print('I found an exception!')