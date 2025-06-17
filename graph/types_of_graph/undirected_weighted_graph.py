class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}  # Dictionary to store adjacency list representation

        # Build the graph as an undirected weighted graph
        for u, v, w in self.edges:
            # Initialize adjacency list for vertex u if not present
            if u not in self.adj_list:
                self.adj_list[u] = []
            # Initialize adjacency list for vertex v if not present
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Add edge from u to v with weight w if not already present
            if [v, w] not in self.adj_list[u]:
                self.adj_list[u].append([v, w])
            # Add edge from v to u with weight w (since undirected)
            if [u, w] not in self.adj_list[v]:
                self.adj_list[v].append([u, w])

    def get_adj_list(self):
        # Print the adjacency list for each vertex
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")

    def add_vertex(self, u):
        # Add a new vertex u with an empty adjacency list, if it doesn't exist
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge(self, edge):
        u, v, w = edge

        # Ensure both vertices exist in the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add edge u -> v with weight w if not present
        if [v, w] not in self.adj_list[u]:
            self.adj_list[u].append([v, w])
        # Add edge v -> u with weight w (undirected graph)
        if [u, w] not in self.adj_list[v]:
            self.adj_list[v].append([u, w])

    def delete_vertex(self, target):
        # Remove all edges pointing to the target vertex from all adjacency lists
        for node in self.adj_list:
            self.adj_list[node] = [[v, w] for v, w in self.adj_list[node] if v != target]

        # Remove the target vertex from the adjacency list dictionary
        if target in self.adj_list:
            del self.adj_list[target]

    def delete_edge(self, edge):
        u, v, w = edge

        # Remove edge u -> v with weight w if it exists
        if u in self.adj_list and [v, w] in self.adj_list[u]:
            self.adj_list[u].remove([v, w])
        # Remove edge v -> u with weight w for undirected graph
        if v in self.adj_list and [u, w] in self.adj_list[v]:
            self.adj_list[v].remove([u, w])

# Example usage
edges = [
    ["A", "D", 3],
    ["A", "E", 3],
    ["A", "C", 3],
    ["B", "F", 2],
    ["C", "E", 4],
    ["C", "G", 5],
    ["C", "B", 3],
    ["C", "F", 4],
]

graph = Graph(edges)
graph.get_adj_list()  # Print initial graph

graph.add_vertex("H")  # Add vertex H
graph.get_adj_list()  # Print updated graph

graph.add_edge(["G", "H", 10])  # Add edge G-H with weight 10
graph.get_adj_list()  # Print updated graph

graph.delete_vertex("A")  # Delete vertex A and all its edges
graph.get_adj_list()  # Print updated graph

graph.delete_edge(["C", "E", 4])  # Delete edge C-E with weight 4
graph.get_adj_list()  # Print updated graph
