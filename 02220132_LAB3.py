class ArrayStack:
    def __init__(self, capacity=10):
        self._stack = [None] * capacity  
        self._top = -1  
        self._capacity = capacity
        print(f"Created new ArrayStack with capacity: {capacity}")
        print(f"Stack is empty: {self.is_empty()}")

    def push(self, element):
        if self.size() == self._capacity:
            self._resize(2 * self._capacity)  
        self._top += 1
        self._stack[self._top] = element
        print(f"Pushed {element} to the stack")
        self.display()

    def pop(self):
        if self.is_empty():
            print("Stack underflow! Cannot pop from an empty stack.")
            return None
        element = self._stack[self._top]
        self._stack[self._top] = None  
        self._top -= 1
        print(f"Popped element: {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty. No top element.")
            return None
        print(f"Top element: {self._stack[self._top]}")
        return self._stack[self._top]

    def is_empty(self):
        return self._top == -1

    def size(self):
        return self._top + 1

    def display(self):
        if self.is_empty():
            print("Display stack: []")
        else:
            elements = self._stack[:self._top + 1]
            print(f"Display stack: {elements}")

    def _resize(self, new_capacity):
        new_stack = [None] * new_capacity
        for i in range(self._top + 1):
            new_stack[i] = self._stack[i]
        self._stack = new_stack
        self._capacity = new_capacity
        print(f"Resized stack to new capacity: {new_capacity}")

if __name__ == "__main__":
    stack = ArrayStack()

    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    stack.pop()
    print(f"Stack size: {stack.size()}")
    stack.display()
