class DisjointSet:
    def __init__(self, n):
        # Initialize the parent list where each node is its own parent
        self.parent = [i for i in range(n)]

    def find(self, i):
        # Recursively find the root of the set that i belongs to
        # (without path compression)
        if i == self.parent[i]:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        # Find the roots of the sets that x and y belong to
        x_root = self.find(x)
        y_root = self.find(y)

        # If they are in different sets, merge them
        if x_root != y_root:
            self.parent[y_root] = x_root  # Make x_root the parent of y_root

    def display(self):
        # Return the current parent array representing the sets
        return self.parent

# Create a disjoint set with 8 elements (0 through 7)
ds = DisjointSet(8)

# Merge sets: {0,1}, {2,3}, {4,5}, {6,7}
ds.union(0, 1)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)

# Merge sets: {0,1,2,3}, {4,5,6,7}
ds.union(0, 2)
ds.union(4, 6)

# Display the parent list (not the actual groupings but useful for debugging)
print(ds.display())

# Find and print the root representative of element 3
print(ds.find(3))

# Find and print the root representative of element 7
print(ds.find(7))

# Merge all into one set: {0,1,2,3,4,5,6,7}
ds.union(0, 4)

# Display the parent list (not the actual groupings but useful for debugging)
print(ds.display())

# Find the root representative of element 3
print(ds.find(3))

# Find the root representative of element 7
print(ds.find(7))
