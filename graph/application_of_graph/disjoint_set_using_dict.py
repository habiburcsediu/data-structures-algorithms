class DisjointSetUnion:
    def __init__(self):
        # Dictionary to store the parent of each node
        self.parent = {}
        # Dictionary to store the rank (approximate tree height) of each node
        self.rank = {}

    def find(self, node):
        # If node is not present, initialize it as its own parent (singleton set)
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 0
        
        # Path compression: recursively find root parent and update parent's reference
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        # Return the representative (root) of the set this node belongs to
        return self.parent[node]

    def union(self, u, v):
        # Find the root parents of u and v
        root_u = self.find(u)
        root_v = self.find(v)

        # If both nodes share the same root, they are already connected
        if root_u == root_v:
            return

        # Union by rank:
        # Attach the smaller ranked tree under the larger ranked one
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        elif self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        else:
            # If ranks are equal, choose one as parent and increment its rank
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

    def display(self):
        # Return the current parent mapping for debugging or inspection
        return self.parent


# Example usage
dsu = DisjointSetUnion()

dsu.union(0, 1)
print(dsu.display())  # Expected: {0: 0, 1: 0}

dsu.union(2, 3)
print(dsu.display())  # Expected: {0: 0, 1: 0, 2: 2, 3: 2}

dsu.union(1, 3)
print(dsu.display())  # Expected: parents merged appropriately
