class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        """Return True if the stack is empty"""

        return len(self.stack) == 0

    def push(self, val):
        """Push an item onto the stack"""

        self.stack.append(val)

    def pop(self):
        """Remove and return the top item of the stack"""

        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop item!")

        return self.stack.pop()

    def peek(self):
        """Return the top item from the stack without removing it"""

        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek item!")

        return self.stack[-1]

    def display(self):
        """Return a list of items of stack from top to bottom"""

        return self.stack[::-1]

# Example usage
stack = Stack()

try:
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack.display()) # [30, 20, 10]

    stack.pop()
    print(stack.display()) # [20, 10]

    stack.peek() # 20
except Exception as obj:
    print(obj)


