def merge_sort(arr):
    comparisons = 0
    accesses = 0

    def merge(left, right):
        nonlocal comparisons, accesses
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1  # Comparing elements
            accesses += 2     # Accessing left[i] and right[j]
            if left[i] <= right[j]:
                merged.append(left[i])
                accesses += 1  # Appending to merged
                i += 1
            else:
                merged.append(right[j])
                accesses += 1
                j += 1

        # Add remaining elements
        while i < len(left):
            merged.append(left[i])
            accesses += 1
            i += 1
        while j < len(right):
            merged.append(right[j])
            accesses += 1
            j += 1

        return merged

    def sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        mid = len(sub_arr) // 2
        left = sort(sub_arr[:mid])
        right = sort(sub_arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return sorted_arr, comparisons, accesses


# Example usage
original = [38, 27, 43, 3, 9, 82, 10]
sorted_list, comps, accs = merge_sort(original)

print("Original List:", original)
print("Sorted using Merge Sort:", sorted_list)
print("Number of comparisons:", comps)
print("Number of array accesses:", accs)
