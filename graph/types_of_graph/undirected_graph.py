class Graph:
    def __init__(self, edges):
        self.edges = edges              # Store the list of edges
        self.adj_list = {}              # Initialize an empty adjacency list

        for u, v in self.edges:
            # Add nodes to the adjacency list if they aren't already present
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Add the undirected edge, avoiding duplicates
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def get_adj_list(self):
        # Print the adjacency list for each node
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")  # Empty line for readability

    def add_vertex(self, u):
        # Add a new vertex with an empty neighbor list if it doesn't exist
        if u not in self.adj_list:
            self.adj_list[u] = []

    def add_edge(self, edge):
        u, v = edge

        # Ensure both vertices exist in the adjacency list
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        # Add the edge in both directions, avoiding duplicates
        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def delete_vertex(self, target):
        # Remove all edges pointing to the target vertex
        for node in self.adj_list:
            if target in self.adj_list[node]:
                # Keep only neighbors that are not the target
                self.adj_list[node] = [v for v in self.adj_list[node] if v != target]

        # Finally, delete the target vertex itself
        if target in self.adj_list:
            del self.adj_list[target]

    def delete_edge(self, edge):
        u, v = edge

        # Remove v from u's neighbor list if the edge exists
        if u in self.adj_list and v in self.adj_list[u]:
            self.adj_list[u].remove(v)

        # Remove u from v's neighbor list if the edge exists
        if v in self.adj_list and u in self.adj_list[v]:
            self.adj_list[v].remove(u)

# Sample usage
edges = [
    ["A", "B"],
    ["A", "C"],
    ["A", "D"],
    ["B", "C"],
    ["C", "D"],
    ["C", "E"]
]

graph = Graph(edges)

graph.get_adj_list()             # Print initial adjacency list

graph.add_vertex("F")            # Add a new vertex 'F'
graph.get_adj_list()             # Print updated graph

graph.add_edge(["D", "F"])       # Add an edge between D and F
graph.get_adj_list()             # Print updated graph

graph.delete_vertex("F")         # Delete vertex F and its connections
graph.get_adj_list()             # Print updated graph

graph.delete_edge(["C", "E"])    # Delete edge between C and E
graph.get_adj_list()             # Final graph state
