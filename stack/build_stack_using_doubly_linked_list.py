# Define a doubly linked list node
class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        """Check if the stack is empty or not"""

        return self.tail is None

    def push(self, val):
        """Push an item onto the stack"""

        new_node = ListNode(val) # Create a new node

        if self.is_empty():
            # If stack is empty
            self.head = new_node
            self.tail = new_node
        else:
            # If stack is not empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        """Remove and return the top item from the stack"""

        if self.is_empty():
            raise Exception("Stack is empty. Cannot pop item!")

        top_item = self.tail.val # Store the top item to return later


        if self.head == self.tail:
            # Only one item in the stack
            self.head = None
            self.tail = None
        else:
            # More than one item in the stack
            self.tail.prev.next = None
            self.tail = self.tail.prev

        return top_item

    def peek(self):
        """Return the top item from the stack without removing it"""

        if self.is_empty():
            raise Exception("Stack is empty. Cannot peek item!")

        return self.tail.val

    def display(self):
        """Return a list of stack items from top to bottom (LIFO order)"""

        if self.is_empty():
            raise Exception("Stack is empty. Nothing to show!")

        result = []
        current = self.tail
        while current:
            result.append(current.val)
            current = current.prev

        return result

# Example usage
stack = Stack()

# Pushing items onto the stack
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack (top to bottom):", stack.display())

print("Popped:", stack.pop())
print("Stack after pop:", stack.display())

print("Peek top:", stack.peek())


