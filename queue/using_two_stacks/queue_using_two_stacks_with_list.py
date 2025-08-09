"""
LeetCode Problem: 232. Implement Queue using Stacks
URL             : https://leetcode.com/problems/implement-queue-using-stacks/

Problem:
    Implement a queue using two stacks.
    You must implement the following operations of a queue:
    - push(x): Push element x to the back of the queue.
    - pop(): Removes the element from the front of the queue and returns it.
    - peek(): Get the front element.
    - empty(): Returns whether the queue is empty.

    You can only use standard stack operations: push to top, peek/pop from top, size, and is empty.
    The operations must simulate FIFO behavior using LIFO stacks efficiently.
"""


# ------------------------------ 1. Using List ------------------------------ #
"""
Approach:
- Use two stacks, `input` and `output`.
- For `push(x)`: Append the element to the `input` stack.
- For `pop()` and `peek()`:
    - If `output` stack is empty, transfer all elements from `input` stack to `output` stack,
      reversing the order to simulate FIFO queue behavior.
    - Then pop or peek from the `output` stack.
- `empty()` checks if both stacks are empty.

Time Complexity:
- `push()`: O(1) amortized.
- `pop()`: Amortized O(1) — transferring elements happens only when `output` is empty.
- `peek()`: Amortized O(1).
- `empty()`: O(1).

Space Complexity:
- O(n), where n is the number of elements in the queue (stored in the two stacks).
"""

class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()

        return self.output.pop()

    def peek(self) -> int:
        # In the problem statement, they guarantee you that all calls to pop and peek are valid —
        # meaning they will never be called on an empty queue.
        # So in LeetCode, you don’t need to handle the "empty" case.
        # Transfer only when output stack is empty
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())

        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output

    def display(self):
        self.peek()

        result = list(reversed(self.output))
        print(result)

# Example usage
queue = MyQueue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.display() # Output: [10, 20, 30]

queue.pop()
queue.display() # Output: [20, 30]

print(queue.peek()) # Output : 20