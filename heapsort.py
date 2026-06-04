# heapsort.py

# --------------------------------------------------
# HEAPSORT IMPLEMENTATION
# --------------------------------------------------

# Heapify function
# Maintains the max-heap property
def heapify(arr, n, i):

    # Assume root is largest
    largest = i

    # Calculate left child index
    left = 2 * i + 1

    # Calculate right child index
    right = 2 * i + 2

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:

        # Swap values
        arr[i], arr[largest] = arr[largest], arr[i]

        # Continue heapifying
        heapify(arr, n, largest)


# Build max heap
def build_max_heap(arr):

    n = len(arr)

    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):

        heapify(arr, n, i)


# Heapsort algorithm
def heapsort(arr):

    n = len(arr)

    # Build max heap
    build_max_heap(arr)

    # Extract largest element repeatedly
    for i in range(n - 1, 0, -1):

        # Move largest element to end
        arr[0], arr[i] = arr[i], arr[0]

        # Restore heap property
        heapify(arr, i, 0)

    return arr


# --------------------------------------------------
# TEST PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    numbers = [12, 11, 13, 5, 6, 7]

    print("Original Array:")
    print(numbers)

    heapsort(numbers)

    print("\nSorted Array:")
    print(numbers)