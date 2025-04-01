##
# Michael Ghattas
# COMP 4581 - Lab 5
# Feb/10/2025
##



from collections import deque


class CircularQueue:
    def __init__(self, capacity):
        """Initialize the circular queue with a fixed capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity  # Fixed-size list
        self.front = self.rear = -1  # Pointers to track front and rear

    def enqueue(self, value):
        """Add an element to the queue."""
        if (self.rear + 1) % self.capacity == self.front:
            raise OverflowError("Queue is full")  # Circular queue is full

        if self.empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = value

    def dequeue(self):
        """Remove and return the front element from the queue."""
        if self.empty():
            raise IndexError("Dequeue from an empty queue")

        value = self.queue[self.front]
        if self.front == self.rear:  # Queue becomes empty after removal
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        return value

    def front_element(self):
        """Return the front element without removing it."""
        if self.empty():
            raise IndexError("Front from an empty queue")
        return self.queue[self.front]

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.front == -1

    def __str__(self):
        """Return a string representation of the queue."""
        if self.empty():
            return "Queue is empty"

        result = []
        i = self.front
        while True:
            result.append(str(self.queue[i]))
            if i == self.rear:
                break
            i = (i + 1) % self.capacity

        return " <- ".join(result)



class MaxHeap:
    def __init__(self):
        """Initialize an empty max heap."""
        self.heap = []

    def insert(self, value):
        """Insert a new value into the heap and maintain heap property."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """Remove and return the maximum element (root of the heap)."""
        if not self.heap:
            raise IndexError("Extract from an empty heap")

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Replace root with last element
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        """Restore the heap property after insertion."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Restore the heap property after removal."""
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def max(self):
        """Return the maximum element without removing it."""
        if not self.heap:
            raise IndexError("Max from an empty heap")
        return self.heap[0]

    def empty(self):
        """Return True if the heap is empty, False otherwise."""
        return len(self.heap) == 0

    def __str__(self):
        """Return a string representation of the heap."""
        return str(self.heap)


# Testing Circular Queue
cq = CircularQueue(5)
print(cq.empty())  # True
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print(cq)  # 10 <- 20 <- 30
print(cq.dequeue())  # 10
print(cq)  # 20 <- 30
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)
print(cq)  # 20 <- 30 <- 40 <- 50 <- 60


# Testing MaxHeap
heap = MaxHeap()
heap.insert(10)
heap.insert(20)
heap.insert(15)
heap.insert(40)
heap.insert(50)
print(heap)  # [50, 40, 15, 10, 20] (Heap structure varies based on inserts)
print(heap.extract_max())  # 50
print(heap)  # [40, 20, 15, 10]



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##