# create a node for singly linked list
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# create a singly linked list
class SinglyLinkedList:
    def __init__(self):
        self.head = None # initially, head is none

    # insert at the end
    def append(self, val):
        # create a new node
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
        else:
            if self.head.next is None:
                self.head.next = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next

                current.next = new_node

    # insert at the beginning
    def prepend(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at any position
    def insert(self, val, position):
        if position < 0:
            print("Invalid position. Position must be zero or greater than zero!")
            return

        new_node = ListNode(val)
        if position == 0:
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head = new_node
        else:
            prev_node = None
            current = self.head
            current_position = 0
            while current.next and current_position < position:
                prev_node = current
                current = current.next
                current_position += 1

            if current.next is None:
                print("Position is out of range!")
                return

            prev_node.next = new_node
            new_node.next = current

    # deleted by value
    def deleted_by_value(self, val):
        current = self.head
        if current.val == val:
            self.head = current.next
        else:
            prev_node = None
            while current.val !=  val:
                prev_node = current
                current = current.next

            prev_node.next = current.next

    def display(self):
        if self.head is None:
            print("Linked list is empty. Nothing to show!")
        else:
            current = self.head

            print("Linked list: ", end="")
            while current:
                print(current.val, end=" -> ")
                current = current.next
            print("None")

singly_linked_list = SinglyLinkedList()
singly_linked_list.append(10)
singly_linked_list.append(20)
singly_linked_list.append(30)

singly_linked_list.display()


singly_linked_list.prepend(400)
singly_linked_list.prepend(500)

singly_linked_list.display()


singly_linked_list.insert(800, 5)

singly_linked_list.display()


singly_linked_list.deleted_by_value(20)

singly_linked_list.display()