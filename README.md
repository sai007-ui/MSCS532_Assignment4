# MSCS532 Assignment 4: Heap Data Structures – Implementation, Analysis, and Applications

## Overview

This project focuses on the implementation, analysis, and application of heap-based data structures. The assignment includes the implementation of the Heapsort algorithm, performance comparison with Merge Sort, and the development of a Priority Queue using a binary max-heap. The project demonstrates how heap data structures provide efficient solutions for sorting and task scheduling problems.

---

## Project Structure

```text
MSCS532_Assignment4
│
├── heapsort.py
├── priority_queue.py
├── comparison.py
├── README.md
└── Assignment4_Report.docx
```

### File Descriptions

* **heapsort.py** – Implements the Heapsort algorithm using a binary max-heap.
* **priority_queue.py** – Implements a Priority Queue using a binary max-heap and a Task class.
* **comparison.py** – Compares the execution times of Heapsort and Merge Sort.
* **Assignment4_Report.docx** – Contains theoretical analysis, experimental results, implementation details, and conclusions.

---

## Requirements

* Python 3.x
* Visual Studio Code (recommended)

Verify your Python installation:

```bash
python --version
```

---

## Running the Programs

### 1. Heapsort Implementation

Run the following command:

```bash
python heapsort.py
```

Expected Output:

```text
Original Array:
[12, 11, 13, 5, 6, 7]

Sorted Array:
[5, 6, 7, 11, 12, 13]
```

---

### 2. Priority Queue Implementation

Run the following command:

```bash
python priority_queue.py
```

Expected Output:

```text
Highest Priority Task:
Task ID: 2, Priority: 10, Arrival Time: 1, Deadline: 15
```

---

### 3. Sorting Performance Comparison

Run the following command:

```bash
python comparison.py
```

Sample Output:

```text
==================================================
Array Size: 100
==================================================
Heapsort: 0.001308 sec
Merge Sort: 0.000925 sec

==================================================
Array Size: 300
==================================================
Heapsort: 0.001521 sec
Merge Sort: 0.001163 sec

==================================================
Array Size: 500
==================================================
Heapsort: 0.009548 sec
Merge Sort: 0.007584 sec
```

---

## Experimental Results

| Array Size | Heapsort (sec) | Merge Sort (sec) |
| ---------- | -------------- | ---------------- |
| 100        | 0.001308       | 0.000925         |
| 300        | 0.001521       | 0.001163         |
| 500        | 0.009548       | 0.007584         |

The experimental results show that both algorithms scale efficiently as the input size increases. Merge Sort performed slightly faster than Heapsort in all test cases; however, Heapsort maintained its guaranteed O(n log n) running time while requiring only constant auxiliary space.

---

## Time Complexity Analysis

### Heapsort

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n log n)      |
| Average Case | O(n log n)      |
| Worst Case   | O(n log n)      |

Heapsort first builds a max-heap in O(n) time and then performs n extraction operations, each requiring O(log n) time. As a result, the overall complexity remains O(n log n) regardless of input distribution.

### Space Complexity

* Auxiliary Space: O(1)
* In-place sorting algorithm
* No additional arrays required

---

## Priority Queue Operations

The priority queue is implemented using a binary max-heap stored in a Python list.

| Operation    | Time Complexity |
| ------------ | --------------- |
| Insert       | O(log n)        |
| Extract Max  | O(log n)        |
| Increase Key | O(log n)        |
| Is Empty     | O(1)            |

The array-based heap representation provides efficient access to parent and child nodes using index calculations while minimizing memory overhead.

---

## Design Choices

A binary max-heap was selected because it efficiently supports priority-based scheduling. Tasks with higher priority values are processed before lower-priority tasks. The heap is implemented using a Python list because array-based heaps are simple to implement and provide efficient memory utilization.

The Task class stores the following information:

* Task ID
* Priority
* Arrival Time
* Deadline

This structure allows the priority queue to simulate task scheduling scenarios commonly found in operating systems and real-time applications.

---

## Applications of Heaps and Priority Queues

Heap data structures and priority queues are widely used in:

* Operating system task scheduling
* CPU process management
* Network packet routing
* Event-driven simulations
* Graph algorithms such as Dijkstra’s Algorithm
* Job scheduling systems

These applications benefit from the efficient insertion and removal of high-priority elements.

---

## Conclusion

This project demonstrated the implementation and analysis of Heapsort and Priority Queues using binary heaps. Experimental testing confirmed the theoretical O(n log n) performance of Heapsort across different input sizes. The priority queue successfully maintained task priorities while supporting efficient insertion and extraction operations. Overall, heap-based data structures provide predictable performance and are essential components of many real-world computing systems.
