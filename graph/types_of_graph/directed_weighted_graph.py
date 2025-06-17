class Graph:
    def __init__(self, edges):
        self.edges = edges            # Store the list of input edges
        self.adj_list = {}            # Initialize an empty adjacency list

        # Build the adjacency list from the edges
        for u, v, w in self.edges:
            if u not in self.adj_list:
                self.adj_list[u] = []     # Add u to adj_list if not present
            if v not in self.adj_list:
                self.adj_list[v] = []     # Add v to adj_list to ensure all nodes are present

            # Add the edge u -> v with weight w, avoiding duplicates
            if [v, w] not in self.adj_list[u]:
                self.adj_list[u].append([v, w])

    def get_adj_list(self):
        # Print the adjacency list in a readable format
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")  # For better spacing

    def add_vertex(self, u):
        # Add a new vertex to the graph if it doesn't already exist
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge(self, edge):
        u, v, w = edge

        # Ensure both u and v exist in the graph
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add the new edge u -> v with weight w if not already present
        if [v, w] not in self.adj_list[u]:
            self.adj_list[u].append([v, w])

    def delete_vertex(self, target):
        # Remove all incoming edges to the target vertex
        for node in self.adj_list:
            self.adj_list[node] = [[v, w] for v, w in self.adj_list[node] if v != target]

        # Remove the target vertex from the graph
        if target in self.adj_list:
            del self.adj_list[target]

    def delete_edge(self, edge):
        u, v, w = edge

        # If the edge u -> v with weight w exists, remove it
        if u in self.adj_list and [v, w] in self.adj_list[u]:
            self.adj_list[u].remove([v, w])

# Example usage
edges = [
    ["A", "D", 3],
    ["A", "E", 3],
    ['A', "C", 3],
    ["B", "F", 2],
    ["C", "B", 3],
    ["C", "F", 4],
    ["E", "C", 4],
    ["G", "C", 5]
]
graph = Graph(edges)
graph.get_adj_list()                # Initial graph

graph.add_vertex("H")               # Add isolated node
graph.get_adj_list()

graph.add_edge(["G", "H", 3])       # Add edge from G to H
graph.get_adj_list()

graph.delete_vertex("H")            # Delete vertex H and all related edges
graph.get_adj_list()

graph.delete_edge(["G", "C", 5])    # Delete edge G -> C (5)
graph.get_adj_list()
