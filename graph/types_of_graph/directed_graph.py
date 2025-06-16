class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        # Build the adjacency list from the given edges
        for u, v in self.edges:
            # Ensure both nodes exist in the adjacency list
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Add the edge from u to v (directed graph), avoiding duplicates
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)

    def get_adj_list(self):
        # Print the adjacency list
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")

    def add_vertex(self, u):
        # Add a new vertex if it doesn't exist
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge(self, edge):
        u, v = edge

        # Ensure both vertices exist before adding the edge
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add the edge from u to v (directed graph), avoiding duplicates
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

    def delete_vertex(self, target):
        # Remove all incoming edges to the target node
        for node in self.adj_list:
            if target in self.adj_list[node]:
                self.adj_list[node] = [v for v in self.adj_list[node] if v != target]

        # Remove the target node from the graph
        if target in self.adj_list:
            del self.adj_list[target]

    def delete_edge(self, edge):
        u, v = edge

        # Remove the edge from u to v if it exists
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

# Example usage
edges = [
    ["A", "B"],
    ["A", "D"],
    ["B", "A"],
    ["B", "C"],
    ["C", "A"],
    ["C", "D"],
    ["D", "A"]
]

graph = Graph(edges)

graph.get_adj_list()        # Display initial adjacency list

graph.add_vertex("E")       # Add new vertex 'E'
graph.get_adj_list()

graph.add_edge(["C", "E"])  # Add edge from C to E
graph.get_adj_list()

graph.delete_vertex("A")    # Remove vertex 'A' and related edges
graph.get_adj_list()

graph.delete_edge(["C", "D"])  # Remove edge from C to D
graph.get_adj_list()
