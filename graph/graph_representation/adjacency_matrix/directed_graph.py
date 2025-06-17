class Graph:
    def __init__(self, edges):
        self.edges = edges

        # Collect and sort all unique nodes from edges
        self.unique_nodes = sorted(set(u for u, v in self.edges) | set(v for u, v in self.edges))

        # Map each unique node to an index for matrix representation
        self.node_to_index = {node: i for i, node in enumerate(self.unique_nodes)}

        # Initialize adjacency matrix of size n x n filled with zeros
        n = len(self.unique_nodes)
        self.adj_matrix = [[0] * n for _ in range(n)]

        # Fill the adjacency matrix, 1 indicates an edge from u to v
        for u, v in self.edges:
            i = self.node_to_index[u]
            j = self.node_to_index[v]
            self.adj_matrix[i][j] = 1

    def get_adj_matrix(self):
        for row in graph.adj_matrix:
            print(row)

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
graph.get_adj_matrix()
