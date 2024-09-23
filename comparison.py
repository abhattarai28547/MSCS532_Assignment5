from deterministic_quicksort import quicksort
from randomized_quicksort import randomized_quicksort
import random
import time


def time_quicksort(sort_function, arr):
    """Times the sorting function."""
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def run_experiments():
    sizes = [1000, 5000, 10000, 50000, 100000]
    results = []

    for size in sizes:
        random_array = [random.randint(0, 10000) for _ in range(size)]
        sorted_array = list(range(size))
        reverse_sorted_array = list(range(size, 0, -1))

        # Timing Deterministic Quicksort
        time_det_random = time_quicksort(quicksort, random_array.copy())
        time_det_sorted = time_quicksort(quicksort, sorted_array.copy())
        time_det_reverse_sorted = time_quicksort(quicksort, reverse_sorted_array.copy())

        # Timing Randomized Quicksort
        time_rand_random = time_quicksort(randomized_quicksort, random_array.copy())
        time_rand_sorted = time_quicksort(randomized_quicksort, sorted_array.copy())
        time_rand_reverse_sorted = time_quicksort(randomized_quicksort, reverse_sorted_array.copy())

        results.append({
            "size": size,
            "det_random": time_det_random,
            "det_sorted": time_det_sorted,
            "det_reverse_sorted": time_det_reverse_sorted,
            "rand_random": time_rand_random,
            "rand_sorted": time_rand_sorted,
            "rand_reverse_sorted": time_rand_reverse_sorted
        })

    return results

def print_results(results):
    print(f"{'Array Size':<12} {'Algorithm':<15} {'Random Array':<15} {'Sorted Array':<15} {'Reverse-Sorted Array':<20}")
    for result in results:
        print(f"{result['size']:<12} {'Deterministic':<15} {result['det_random']:.6f}s {result['det_sorted']:.6f}s {result['det_reverse_sorted']:.6f}s")
        print(f"{result['size']:<12} {'Randomized':<15} {result['rand_random']:.6f}s {result['rand_sorted']:.6f}s {result['rand_reverse_sorted']:.6f}s")

if __name__ == "__main__":
    experiment_results = run_experiments()
    print_results(experiment_results)