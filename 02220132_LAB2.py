# File Name: YourStudentNo_LAB2.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        print("Created new LinkedList")
        print(f"Size: {self.count}")
        print(f"Head: {self.head}")

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        print(f"Appended: {element}")

    def prepend(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        print(f"Prepended: {element}")

    def get(self, index):
        if index < 0 or index >= self.count:
            print("Index out of range")
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        print(f"Element at index {index}: {current.data}")
        return current.data

    def set(self, index, element):
        if index < 0 or index >= self.count:
            print("Index out of range")
            return
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = element
        print(f"Set index {index} to {element}")

    def size(self):
        print(f"Size: {self.count}")
        return self.count

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("List: [" + " ".join(elements) + "]")

if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(5)
    my_list.get(0)
    my_list.set(0, 10)
    my_list.get(0)
    my_list.size()
    my_list.prepend(10)
    my_list.print_list()
