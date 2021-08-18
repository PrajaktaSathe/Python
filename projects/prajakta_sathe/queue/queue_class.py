class Queue:
    """Program to implement queue data structure in python."""

    def __init__(self):
        """Constructor to initialize a queue."""

        self.items = []

    def enqueue(self, item):
        """Function to enqueue elements."""

        self.items.append(item)

    def dequeue(self):
        """Function to dequeue elements."""

        return self.items.pop(0)

    def display(self):
        """Function to display elements in a queue"""

        print(self.items)
