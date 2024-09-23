def quicksort(arr):
    """Perform quicksort on the given array."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choosing the middle element as the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(sample_array)
    print("Sorted Array (Deterministic):", sorted_array)