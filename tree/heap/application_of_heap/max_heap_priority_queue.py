class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, i):
        """Helper function to restore max-heap property from current node to root"""

        parent = (i - 1) // 2
        while parent >= 0 and self.heap[parent][1] < self.heap[i][1]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]

            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        """Helper function to restore max-heap property from current node to subtree"""

        largest = i
        left = (2 * i) + 1
        right = (2 * i) + 2

        n = len(self.heap)

        if left < n and self.heap[largest][1] < self.heap[left][1]:
            largest = left

        if right < n and self.heap[largest][1] < self.heap[right][1]:
            largest = right

        if largest != i:
            self.heap[largest], self.heap[i] = self.heap[i], self.heap[largest]
            self._heapify_down(largest)

    def _extract_max(self):
        """Helper function to return and remove the root element (maximum in max-heap) from the heap"""

        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the root element (maximum in max-heap) to return later
        max_item = self.heap[0]

        # Replace root node with last node and remove last node
        last_item = self.heap.pop()
        self.heap[0] = last_item

        # Restore the max-heap property after deleting the root element everytime
        self._heapify_down(0)

        return max_item

    def enqueue(self, item, priority):
        """Push an item to the priority queue and restore the max-heap property based on its priority"""

        self.heap.append((item, priority)) # Push an item in the queue

        self._heapify_up(len(self.heap) - 1) # Restore the max-heap property

    def dequeue(self):
        """Remove and return the item with the highest priority value from the priority queue"""
        return self._extract_max()

    def peek(self):
        """Peek the top element without removing it"""

        if not self.heap:
            return None
        return self.heap[0]

# Example usage
pq = PriorityQueue()

pq.enqueue("Task 1", 10)
pq.enqueue("Task 2", 5)
pq.enqueue("Task 3", 8)
pq.enqueue("Task 4", 12)
print(pq.heap)

print(pq.dequeue())