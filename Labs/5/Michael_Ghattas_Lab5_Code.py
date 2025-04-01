##
# Michael Ghattas
# COMP 4581 - Lab 5
# Feb/10/2025
##



from collections import deque


class MyStack:
    def __init__(self, data_type):
        """Initialize an empty stack."""
        self.stack = []
        self.data_type = data_type

    def push(self, value):
        """Push an element onto the stack."""
        if not isinstance(value, self.data_type):
            raise TypeError("Incorrect data type")
        self.stack.append(value)

    def pop(self):
        """Remove and return the top element from the stack."""
        if self.empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def top(self):
        """Return the top element without removing it."""
        if self.empty():
            raise IndexError("Top from an empty stack")
        return self.stack[-1]

    def empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self.stack) == 0


class MyQueue:
    def __init__(self, data_type):
        """Initialize an empty queue."""
        self.queue = deque()
        self.data_type = data_type

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        if not isinstance(value, self.data_type):
            raise TypeError("Incorrect data type")
        self.queue.append(value)

    def dequeue(self):
        """Remove and return the front element from the queue."""
        if self.empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.popleft()

    def front(self):
        """Return the front element without removing it."""
        if self.empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return len(self.queue) == 0


# Testing Code for Stack
s = MyStack(int)
print(s.empty())  # True
s.push(5)
s.push(8)
print(s.pop())  # 8
s.push(3)
print(s.empty())  # False
print(s.top())  # 3
print(s.pop())  # 3
print(s.pop())  # 5
# print(s.pop())  # Uncommenting this will raise an IndexError

# Testing Code for Queue
q = MyQueue(int)
print(q.empty())  # True
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())  # 5
q.enqueue(3)
print(q.empty())  # False
print(q.front())  # 8
print(q.dequeue())  # 8
print(q.dequeue())  # 3
# print(q.dequeue())  # Uncommenting this will raise an IndexError



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##