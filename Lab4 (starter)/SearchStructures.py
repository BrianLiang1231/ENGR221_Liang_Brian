"""
WRITE YOUR PROGRAM HEADER HERE
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def add(self, item):
        # push to top (top is END of list)
        self.items.append(item)

    def remove(self):
        # pop from top (top is END of list), no pop() allowed
        item = self.items[-1]
        self.items = self.items[:-1]
        return item


# Implementation of a Queue
class Queue():
    def __init__(self):
        self.items = []

    # Returns True if the Queue is empty, or False if it is not empty
    def isEmpty(self):
        return len(self.items) == 0

    # For a Queue, this should "enqueue" item to the end of the Queue
    def add(self, item):
        self.items.append(item)

    # For a Queue, this should "dequeue" an item from the Queue and return it
    def remove(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item