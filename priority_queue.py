# priority_queue.py

# --------------------------------------------------
# TASK CLASS
# --------------------------------------------------

class Task:

    # Constructor
    def __init__(
        self,
        task_id,
        priority,
        arrival_time,
        deadline
    ):

        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    # String representation
    def __str__(self):

        return (
            f"Task ID: {self.task_id}, "
            f"Priority: {self.priority}, "
            f"Arrival Time: {self.arrival_time}, "
            f"Deadline: {self.deadline}"
        )


# --------------------------------------------------
# PRIORITY QUEUE USING MAX HEAP
# --------------------------------------------------

class PriorityQueue:

    # Constructor
    def __init__(self):

        self.heap = []

    # Check if queue is empty
    def is_empty(self):

        return len(self.heap) == 0

    # Insert task
    def insert(self, task):

        self.heap.append(task)

        self.heapify_up(
            len(self.heap) - 1
        )

    # Extract highest priority task
    def extract_max(self):

        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)

        return root

    # Increase task priority
    def increase_key(
        self,
        index,
        new_priority
    ):

        if (
            new_priority
            <= self.heap[index].priority
        ):
            return

        self.heap[index].priority = new_priority

        self.heapify_up(index)

    # Heapify upward
    def heapify_up(self, index):

        while index > 0:

            parent = (index - 1) // 2

            if (
                self.heap[index].priority
                >
                self.heap[parent].priority
            ):

                self.heap[index], self.heap[parent] = (
                    self.heap[parent],
                    self.heap[index]
                )

                index = parent

            else:
                break

    # Heapify downward
    def heapify_down(self, index):

        size = len(self.heap)

        while True:

            largest = index

            left = 2 * index + 1
            right = 2 * index + 2

            if (
                left < size
                and
                self.heap[left].priority
                >
                self.heap[largest].priority
            ):
                largest = left

            if (
                right < size
                and
                self.heap[right].priority
                >
                self.heap[largest].priority
            ):
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = (
                self.heap[largest],
                self.heap[index]
            )

            index = largest


# --------------------------------------------------
# TEST PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    pq = PriorityQueue()

    pq.insert(
        Task(1, 5, 0, 10)
    )

    pq.insert(
        Task(2, 10, 1, 15)
    )

    pq.insert(
        Task(3, 7, 2, 20)
    )

    print(
        "Highest Priority Task:"
    )

    print(
        pq.extract_max()
    )