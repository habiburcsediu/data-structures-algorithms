class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        # Build the adjacency list from edge list
        for u, v in self.edges:
            # Initialize adjacency list entries if not already present
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # For undirected graph, add both directions
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def get_adj_list(self):
        # Print the adjacency list
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")  # Extra newline for better readability

    def bfs(self, start):
        result = []         # Stores BFS traversal order
        visited = set()     # Tracks visited nodes
        queue = [start]     # Queue for BFS traversal

        # Standard BFS loop
        while queue:
            u = queue.pop(0)   # Dequeue front node
            if u in visited:   # Skip if already visited
                continue

            visited.add(u)     # Mark node as visited
            result.append(u)   # Add node to result

            # Enqueue all unvisited and not-in-queue neighbors
            for v in self.adj_list.get(u, []):
                if v not in visited and v not in queue:
                    queue.append(v)

        return result  # Return BFS traversal order


# Example usage
edges = [["A", "B"], ["A", "E"], ["B", "C"], ["B", "E"], ["C", "D"], ["D", "E"]]
graph = Graph(edges)
graph.get_adj_list()         # Print the graph's adjacency list
print(graph.bfs("A"))        # Perform BFS starting from node "A"
