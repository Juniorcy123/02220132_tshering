#Binary serach Implementation
def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1, comparisons  # Target not found
def binary_search_recursive(arr, target, low=0, high=None, comparisons=0):
    if high is None:
        high = len(arr) - 1
    
    if low > high:
        return -1, comparisons  # Target not found
    
    mid = (low + high) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)
# Sample sorted list
arr = [12, 23, 34, 45, 56, 67, 89]
target = 67

# Iterative version
index_iter, comparisons_iter = binary_search_iterative(arr, target)
print(f"Iterative Binary Search:")
print(f"Found at index {index_iter}")
print(f"Number of comparisons: {comparisons_iter}\n")

# Recursive version
index_recur, comparisons_recur = binary_search_recursive(arr, target)
print(f"Recursive Binary Search:")
print(f"Found at index {index_recur}")
print(f"Number of comparisons: {comparisons_recur}")

