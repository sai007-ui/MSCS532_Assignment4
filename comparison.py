# comparison.py

# Import libraries
import random
import time

# Import heapsort
from heapsort import heapsort


# --------------------------------------------------
# MERGE SORT
# --------------------------------------------------

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])

    right = merge_sort(arr[mid:])

    result = []

    i = 0
    j = 0

    while (
        i < len(left)
        and
        j < len(right)
    ):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# --------------------------------------------------
# TIME FUNCTION
# --------------------------------------------------

def time_algorithm(
    algorithm,
    arr
):

    copied = arr.copy()

    start = time.perf_counter()

    algorithm(copied)

    end = time.perf_counter()

    return end - start


# --------------------------------------------------
# PERFORMANCE TEST
# --------------------------------------------------

sizes = [
    100,
    300,
    500
]

for size in sizes:

    random_array = [

        random.randint(
            1,
            1000
        )

        for _ in range(size)

    ]

    heap_time = time_algorithm(
        heapsort,
        random_array
    )

    merge_time = time_algorithm(
        merge_sort,
        random_array
    )

    print("\n" + "=" * 50)

    print(
        f"Array Size: {size}"
    )

    print("=" * 50)

    print(
        f"Heapsort: "
        f"{heap_time:.6f} sec"
    )

    print(
        f"Merge Sort: "
        f"{merge_time:.6f} sec"
    )