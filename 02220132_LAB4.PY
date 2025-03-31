class ArrayQueue:
    def __init__(self, capacity=10):
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, element):
        self.rear += 1
        self.array[self.rear] = element
        self.size += 1
        print(f"Enqueued {element} to the queue")
    
    def dequeue(self):
        if self.size == 0:
            return None
        element = self.array[self.front]
        self.array[self.front] = None
        self.front += 1
        self.size -= 1
        print(f"Dequeued element: {element}")
        return element
    
    def peek(self):
        if self.size == 0:
            return None
        print(f"Front element: {self.array[self.front]}")
        return self.array[self.front]
    
    def size(self):
        return self.size
    
    def display(self):
        if self.size == 0:
            print("Display queue: []")
            return
        current_queue = [x for x in self.array[self.front:self.rear + 1] if x is not None]
        print(f"Display queue: {current_queue}")

queue = ArrayQueue()
print(f"Created new Queue with capacity: {len(queue.array)}")
print(f"Queue is empty: {queue.size == 0}")

queue.enqueue(10)
queue.display()
queue.enqueue(20)
queue.display()
queue.enqueue(30)
queue.display()
queue.peek()
queue.dequeue()
queue.display()
print(f"Queue size: {queue.size}")