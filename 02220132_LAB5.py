def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def main():
    arr = [23, 45, 12, 67, 89, 34, 56]
    target = 67
    print(f"List: {arr}")
    print(f"Searching for {target} using Sequential Search")
    index, comparisons = sequential_search(arr, target)
    if index != -1:
        print(f"Found at index {index}")
    else:
        print("Not found")
    print(f"Number of comparisons: {comparisons}")

if __name__ == "__main__":
    main()