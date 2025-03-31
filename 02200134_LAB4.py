class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        print("Created new LinkedQueue")

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty, cannot dequeue")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return removed_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty, cannot peek")
            return None
        return self.front.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Queue contents:", elements)

queue = LinkedQueue()
print("Queue is empty:", queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print("Peek:", queue.peek())
print("Dequeued:", queue.dequeue())
queue.display()
print("Queue is empty:", queue.is_empty())
# print(f"Size: {queue.size()}")
