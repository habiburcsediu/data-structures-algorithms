class DisjointSet:
    def __init__(self, n):
        # Initialize each node to be its own parent (self loop)
        # and rank (tree depth approximation) to 0
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        # Find the root of the set that element i belongs to
        # Path compression: flatten the tree for faster lookups
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        # Find the roots of the sets x and y belong to
        root_x = self.find(x)
        root_y = self.find(y)

        # If both elements are already in the same set, do nothing
        if root_x == root_y:
            return

        # Union by rank: attach the smaller tree under the bigger one
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1  # Increase rank only if both have the same rank

    def display(self):
        # Return the parent list showing current parent of each element
        return self.parent

# Example usage of DisjointSet
ds = DisjointSet(8)

# Perform unions on pairs of elements
ds.union(0, 1)  # Connect 0 and 1
ds.union(2, 3)  # Connect 2 and 3
ds.union(4, 5)  # Connect 4 and 5
ds.union(6, 7)  # Connect 6 and 7
ds.union(1, 2)  # Connect components {0,1} and {2,3}
ds.union(4, 7)  # Connect components {4,5} and {6,7}

# Uncomment to connect all sets into one:
# ds.union(0, 4)

# Display parent array after unions
print(ds.display())

# Find and print the root of node 3
print(ds.find(3))

# Find and print the root of node 7
print(ds.find(7))
