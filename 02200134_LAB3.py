# Implementation of stack using LinkedList
class Node:
    def __init__(self, element):
        self.data = element
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
        self.size_counter = 0
        print("Created new LinkedStack")

    def is_empty(self):
        return self.head is None

    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
        self.size_counter += 1
        print(f"Pushed {element} onto the stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty, cannot pop")
            return None
        popped_data = self.head.data
        self.head = self.head.next
        self.size_counter -= 1
        print(f"Popped {popped_data} from the stack")
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty, nothing to peek")
            return None
        return self.head.data

    def size(self):
        return self.size_counter

    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        current = self.head
        print("Stack elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example output
stack = LinkedStack()
print("Stack is empty:", stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print("Top element:", stack.peek())
stack.pop()
stack.display()
print("Stack size:", stack.size())
