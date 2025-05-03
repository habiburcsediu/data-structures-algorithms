# Define a node for singly linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Create a singly linked list
class SinglyLinkedList:
    """Implementation of singly linked list"""

    def __init__(self):
        self.head = None # Initially, head is not pointing any node

    def prepend(self, val):
        """Insert a new node with the given value at the beginning of the linked list"""

        # Create a new node
        new_node = ListNode(val)

        # Case 1: If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Case 2: If list is not empty
        new_node.next = self.head
        self.head = new_node

    def append(self, val):
        """Insert a new node with the given value at the end of the singly linked list"""

        new_node = ListNode(val)

        # Case 1: If linked list is empty
        if self.head is None:
            self.head = new_node
            return

        # Case 2: If linked list is not empty
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert(self, val, position):
        """Insert a new node with the given value at the given position of the linked list"""

        # Case 1: If position is less than zero
        if position < 0:
            print("Position is invalid. Position must be zero or greater than zero!")
            return

        new_node = ListNode(val)

        # Case 2: If position is zero
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse through the linked list
        current = self.head
        current_position = 0
        while current and current_position < position - 1:
            current = current.next
            current_position += 1

        # Case 3: Position is out of range
        if current is None:
            print("Position is out of range!")
            return

        # Case 4: If position is valid and greater than zero
        new_node.next = current.next
        current.next = new_node


    def delete_by_value(self, val):
        """Delete a node that is matching with the given value of the linked list"""

        # Case 1: If linked list is empty
        if self.head is None:
            print("Linked list is empty!")
            return

        # Case 2: If value is matching with the head node
        current = self.head
        if current.val == val:
            self.head = current.next
            return

        prev = None
        while current and current.val != val:
            prev = current
            current = current.next

        # Case 3: If value is not found
        if current is None:
            print("Value is not found!")
            return

        # Case 4: If value is matching with any node except head node
        prev.next = current.next

    def delete_at_position(self, position):
        """Delete a node at the given position of the linked list"""

        # Case 1: If position is less than zero
        if position < 0:
            print("Position in invalid. Position must be zero or greater than zero")
            return

        # Case 2: If linked list is empty
        if self.head is None:
            print("Linked list is empty. Can not delete anything!")
            return

        # Case 3: If position is zero (delete head)
        if position == 0:
            self.head = self.head.next
            return


        current = self.head
        current_position = 0
        while current.next and current_position < position - 1:
            current = current.next
            current_position += 1

        # Case 4: Position is out of range
        if current.next is None:
            print("Position is out of range!")
            return

        # Case 5: If position is valid and greater than zero
        current.next = current.next.next

    # Redundant function to display linked list, as I use __str__
    def display(self):
        """Display the linked list"""

        # Case 1: If list is empty
        if self.head is None:
            print("Linked list empty!")
            return

        # Case 2: If list is not empty, traverse the end
        print("Linked list: ", end="")
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def __str__(self):
        if self.head is None:
            return "Linked list is empty!"

        result = []
        current = self.head
        while current:
            result.append(str(current.val)) # ["10", "20", "30"]
            current = current.next

        return " -> ".join(result) + " -> None" # "10 -> 20 -> 30" + " -> None"

# Example
l = SinglyLinkedList()

# Prepend
l.prepend(2)
l.prepend(1)
print(l)

# Append
l.append(3)
l.append(4)
print(l)

# Insert at any position
l.insert(400, 0)
print(l)

# Delete by value
l.delete_by_value(10)
print(l)

# Delete at position
l.delete_at_position(5)
print(l)


