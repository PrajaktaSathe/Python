# Program to implement queue data structure in python - 
class queue:
    # Constructor to initialize a queue
    def __init__(self):
        self.items = []
    
    # Function to enqueue elements - 
    def enqueue(self, item):
        self.items.insert(item)
    
    # Function to dequeue elements -
    def dequeue(self):
        return self.items.pop()

# Function to enqueue element
def enqueue(my_queue):
    item = int(input("Enter element to enqueue: "))
    my_queue.append(item)
 
# Function to dequeue element  
def dequeue(my_queue):    
    print("Dequeued element: " + str(my_queue[0]))
    my_queue.pop(0)

# Function to display elements in a queue  
def display(my_queue):
    print(my_queue)
  
switcher = {
    1: enqueue,
    2: dequeue,
    3: display
}
    
# Function for performing operations on queue  
def queue(my_queue):
    argument = eval(input("Enter 1 to enqueue, 2 to dequeue, 3 to display queue, 4 to exit: "))
    op = switcher.get(argument)
    
    while (argument != 4):
        op(my_queue)
        argument = eval(input("Enter 1 to enqueue, 2 to dequeue, 3 to display queue, 4 to exit: "))
        op = switcher.get(argument)

# Create empty queue        
my_queue = []
# Perform operations on queue
queue(my_queue)
