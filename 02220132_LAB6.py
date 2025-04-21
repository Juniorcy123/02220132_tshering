def partition(arr, low, high, comparisons, swaps):
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort()
    pivot_idx = pivot_candidates[1][1]
    pivot = arr[pivot_idx]
    
    arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
    swaps[0] += 1
    
    i = low - 1
    
    for j in range(low, high):
        comparisons[0] += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            swaps[0] += 1
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    swaps[0] += 1
    return i + 1

def quick_sort_helper(arr, low, high, comparisons, swaps):
    if low < high:
        pi = partition(arr, low, high, comparisons, swaps)
        quick_sort_helper(arr, low, pi - 1, comparisons, swaps)
        quick_sort_helper(arr, pi + 1, high, comparisons, swaps)

def quick_sort(arr):
    comparisons = [0]
    swaps = [0]
    
    arr_copy = arr.copy()
    quick_sort_helper(arr_copy, 0, len(arr_copy) - 1, comparisons, swaps)
    
    return arr_copy, comparisons[0], swaps[0]

if __name__ == "__main__":
    test_list = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original List: {test_list}")
    
    sorted_list, comps, swps = quick_sort(test_list)
    
    print(f"Sorted using Quick Sort: {sorted_list}")
    print(f"Number of comparisons: {comps}")
    print(f"Number of swaps: {swps}")