class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        # Build the adjacency list
        for u, v in self.edges:
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Add edges (undirected graph)
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def get_adj_list(self):
        # Print the adjacency list
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")

    def dfs(self, start):
        result = []            # List to store DFS traversal order
        visited = {start}      # Set to keep track of visited nodes
        stack = [start]        # Stack for DFS (LIFO)

        while stack:
            u = stack.pop()
            result.append(u)

            # Visit neighbors in reverse-sorted order for consistent traversal
            for v in sorted(self.adj_list[u], reverse=True):
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        return result

# Example usage
edges = [["A", "B"], ["A", "E"], ["B", "C"], ["B", "E"], ["C", "D"], ["D", "E"]]
graph = Graph(edges)
graph.get_adj_list()

print(graph.dfs("A"))
