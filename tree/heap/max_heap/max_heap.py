class MaxHeap:
    def __init__(self):
        self.heap = [] # Array to represent complete binary tree for max heap

    def _heapify_down(self, n, i):
        """Helper function to restore max-heap property from node i down to node n"""

        largest = i # Assume, the current node is the largest
        left = (2 * i) + 1 # Index of left child
        right = (2 * i) + 2 # Index of right child

        # If left child exists and is greater than current largest, update largest
        if left < n and self.heap[largest] < self.heap[left]:
            largest = left

        # If right child exists and is greater than current largest, update largest
        if right < n and self.heap[largest] < self.heap[right]:
            largest = right

        if largest != i: # Equal meaning, parent is the largest, no swap
            self.heap[largest], self.heap[i] =  self.heap[i], self.heap[largest]
            self._heapify_down(n, largest) # Continue heapify down the subtree to restore max-heap property

    def _heapify_up(self, i):
        """Helper function to restore max-heap property from node i up to root"""

        parent = (i - 1) // 2 # Find the parent index of the current node for comparing and swapping to maintain max-heap property

        while i > 0 and self.heap[parent] < self.heap[i]: # Compare with parent and swap until the max-heap property is restored
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            i = parent # Move up to the parent's index
            parent = (i - 1) // 2 # Update the parent index for the current node

    def build_heap(self, arr):
        """Build a max-heap from an unsorted array"""

        self.heap = arr[:]
        n = len(arr)
        # Start from the last non-leaf node and heapify each node up to the root
        for i in range((n // 2) - 1, -1, -1):
            self._heapify_down(n, i) # Restore max-heap property by heapify down

    def get_heap(self):
        """Return the array representation of the max-heap"""

        return self.heap # Return the array representation of the max heap

    def add_node(self, val):
        """Insert a value into the max-heap"""

        self.heap.append(val) # Add a new node at the end of the heap
        self._heapify_up(len(self.heap) - 1) # Restore the max-heap property

    def delete_node(self):
        """Delete and return the root element (maximum) from the max-heap"""

        # If the heap is empty, there's nothing to delete
        if not self.heap:
            print("Heap is empty. Can not delete! ")
            return None

        # If there's only one element, just pop and return it
        if len(self.heap) == 1:
            return self.heap.pop() # Remove and return together

        # Store the root element (maximum in a max-heap) to return later
        max_element = self.heap[0]

        # Remove the last node and move to the root position
        self.heap[0] = self.heap.pop()

        # Restore the heap property (max-heap) by heapify down from the root
        self._heapify_down(len(self.heap), 0)

        return max_element

    def peek(self):
        """Return the root element (maximum) of the max-heap without removing it"""

        # If the heap is empty, return None
        if not self.heap:
            return None
        return self.heap[0] # Return the root element (maximum element in the max-heap)

    def heap_sort(self):
        pass

# Example usage
heap = MaxHeap()

arr = [5, 6, 7, 2, 20]
heap.build_heap(arr)
print("Initial heap:", heap.get_heap())

heap.add_node(20)
print("After adding 20:", heap.get_heap())

heap.delete_node()
print("After deletion:", heap.get_heap())

print("Maximum element of the heap:", heap.peek())