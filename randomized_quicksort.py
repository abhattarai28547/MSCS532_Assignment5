import random

def randomized_quicksort(arr):
    """Perform randomized quicksort on the given array."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  # Randomly selecting the pivot
    pivot = arr[pivot_index]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)

# Example usage
if __name__ == "__main__":
    sample_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = randomized_quicksort(sample_array)
    print("Sorted Array (Randomized):", sorted_array)