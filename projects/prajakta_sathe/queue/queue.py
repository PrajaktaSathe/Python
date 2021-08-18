def enqueue(queue: list[int]):
    """Function to enqueue element"""

    item = int(input("Enter element to enqueue: "))
    queue.append(item)


def dequeue(queue: list[int]):
    """Function to dequeue element"""

    print("Dequeued element: ", queue[0])
    queue.pop(0)


def display(queue: list[int]):
    """Function to display elements in a queue"""

    print(queue)


if __name__ == "__main__":
    my_queue = []

    while True:
        choices = ["1", "2", "3", "4"]

        switcher = {
            "1": enqueue,
            "2": dequeue,
            "3": display
        }

        choice = input("Enter 1 to enqueue, 2 to dequeue, 3 to display queue, 4 to exit: ")

        while choice != "4":
            while choice not in choices:
                choice = input("Enter 1 to enqueue, 2 to dequeue, 3 to display queue, 4 to exit: ")
            option = switcher.get(choice)
            option(my_queue)
            choice = input("Enter 1 to enqueue, 2 to dequeue, 3 to display queue, 4 to exit: ")
