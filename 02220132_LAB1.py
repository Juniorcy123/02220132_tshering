class CustomList:
    def __init__(self, initial_capacity=20):
        self._capacity = initial_capacity 
        self._size = 0  
        self._elements = [None] * self._capacity  
        print(f"Created new CustomList with capacity: {self._capacity}")
        print(f"Current size: {self._size}")
    def append(self, element):
        if self._size >= self._capacity:
            print("List is full. Cannot append more elements.")
            return
        self._elements[self._size] = element 
        self._size += 1 
        print(f"Appended {element} to the list")

    def get(self, index):
       
        if index < 0 or index >= self._size:
            print(f"Index {index} is out of bounds.")
            return None
        return self._elements[index]

    def set(self, index, element):
       
        if index < 0 or index >= self._size:
            print(f"Index {index} is out of bounds.")
            return
        self._elements[index] = element  # Replace the element
        print(f"Set element at index {index} to {element}")

    def size(self):
        
        return self._size

    def __str__(self):
       
        return f"CustomList(capacity={self._capacity}, size={self._size}, elements={self._elements[:self._size]})"
if __name__ == "__main__":
    my_list = CustomList()
    my_list.append(5)
    print(f"Element at index 0: {my_list.get(0)}")
    my_list.set(0, 10)
    print(f"Element at index 0: {my_list.get(0)}")
    print(f"Current size: {my_list.size()}")