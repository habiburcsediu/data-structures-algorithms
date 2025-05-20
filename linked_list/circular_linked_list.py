class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def _is_empty(self):
        """Helper function to check whether a list is empty or not"""

        return self.head is None

    def at_begin(self, val):
        """Insert a node at the beginning of a list"""
        
        new_node = ListNode(val) # Create a new node to insert

        # List is empty
        if self._is_empty():
            self.head = new_node
            new_node.next = new_node # Last node points to the first node
            return True
        
        # List is not empty
        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        self.head = new_node

        current.next = new_node # Last node points to the first node
        
        return True

    def at_end(self, val):
        """Insert a node at the end of a list"""

        new_node = ListNode(val)

        # List in empty
        if self._is_empty():
            self.head = new_node
            new_node.next = new_node # Last node points to the first node
            return True
        
        # List is not empty
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head # Last node points to the first node

        return True
        
    def at_any_position(self, position, val):
        """Insert a node at any position of a list"""

        # Position invalid for negative index
        if position < 0:
            print("Position is invalid. Position should be 0 or greater than 0!")
            return False
        
        new_node = ListNode(val)

        # If list is empty and position is 0
        if self._is_empty():
            if position == 0:
                self.head = new_node
                new_node.next = new_node # Last node points to the first node
                return True
            else:
                print("Position is invalid. Position exceeds the size of the list!")
                return False
        
        # If list is not empty and position is 0
        if not self._is_empty() and position == 0:
            current = self.head
            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            self.head = new_node

            current.next = new_node # Last node points to the first node
            return True

        # If list is not empty and size of the list is more than 1
        current = self.head
        current_position = 0
        while current.next != self.head and current_position < position - 1:
            current = current.next
            current_position += 1

        if current_position < position - 1:
            print("Position is invalid. Position exceeds the size of the list!")
            return False
        
        # Insert at any position except first position and at the end
        new_node.next = current.next
        current.next = new_node
        return True
    
    def display(self):
        """Display the list"""

        if self._is_empty():
            print("List is empty!")
            return
        
        current = self.head
        while True:
            print(current.val, end=" -> ")
            current = current.next
        
            if current == self.head:
                break

        print("(Head)")

# Example usage
cl = CircularLinkedList()
cl.display()

# Insert at the beginning
result = cl.at_begin(10)
if result:
    cl.display()

# Insert at the end
result = cl.at_end(20)
if result:
    cl.display()

# Insert at any position
result = cl.at_any_position(-1, 500)
if result:
    cl.display()

result = cl.at_any_position(2, 700)
if result:
    cl.display()