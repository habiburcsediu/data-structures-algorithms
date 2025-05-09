class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, val: any):
        new_node = ListNode(val)

        # If list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        
        # If list is not empty
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, val: any):
        new_node = ListNode(val)

        # If list is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        
        # If list is not empty
        # Don't need to traverse till the end as we know that last node pointer is located in self.tail
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        
    def insert(self, val, position):
        # Case 1
        if position < 0:
            raise Exception("Position is invalid. Should be greater than zero!")
        
        # Case 2
        if position == 0:
            self.prepend(val)
            return

        current = self.head
        current_position = 0
        while current and current_position < position - 1:
            current = current.next
            current_position += 1

        # Case 3
        if not current:
            raise Exception("Position exceeds list size!")

        new_node = ListNode(val)

        new_node.prev = current
        new_node.next = current.next
       
        if current.next:
            current.next.prev = new_node # Case 4: If inserting before the last node
        else:
            self.tail = new_node # Case 5: If inserting after the last node

        current.next = new_node

    def delete_by_value(self, val):
        if not self.head and not self.tail:
            raise Exception("List is empty. Cannot delete!")

        current = self.head

        if current.val == val:
            if not current.next:
                self.head = self.tail =  None
            else:
                self.head = current.next
                current.next.prev = None

            return

        while current and current.val != val:
            current = current.next

        if not current:
            raise Exception(f"{val} is not found. Cannot delete!")

        if current.next is None:
            current.prev.next = None
            self.tail = current.prev
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def display(self, choice = "forward"):
        if choice == "forward":
            current = self.head
            result = []

            while current:
                result.append(str(current.val))
                current = current.next

            return "None" if not result else " <-> ".join(result) + " <-> None"
        
        elif choice == "backward":
            current = self.tail
            result = []
            while current:
                result.append(str(current.val))
                current = current.prev
            return "None" if not result else " <-> ".join(result) + " <-> None"
        
        else:
            raise Exception("Invalid choice. Use 'forward' or 'backward'")

        
    def display(self, choice = "forward"):
        if choice == "forward":
            current = self.head
            result = []

            while current:
                result.append(str(current.val))
                current = current.next

            return "None" if not result else " <-> ".join(result) + " <-> None"
        
        elif choice == "backward":
            current = self.tail
            result = []
            while current:
                result.append(str(current.val))
                current = current.prev
            return "None" if not result else " <-> ".join(result) + " <-> None"
        
        else:
            raise Exception("Invalid choice. Use 'forward' or 'backward'")


# Example usage
l = DoublyLinkedList()

# Display the list
print("List:", l.display())

# Append into the list
l.append(10)
l.append(20)
l.append(30)
print("After appending:", l.display())

# Prepend into the list
l.prepend(400)
print("After prepending:", l.display())

# Insert at the list
try:
    l.insert(700, 10)
except Exception as obj:
    print(obj)
print("After inserting:", l.display())

# Delete by value
val = 10
try:
    l.delete_by_value(val)
except Exception as obj:
    print(obj)
else:
    print(f"{val} is successfully deleted!")
finally:
    print(f"After deleting {val}:", l.display())