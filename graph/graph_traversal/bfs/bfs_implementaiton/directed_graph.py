class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.adj_list = {}

        # Build the adjacency list from the list of edges
        for u, v in self.edges:
            # If node u or v is not already in the adjacency list, add it with an empty list
            if u not in self.adj_list:
                self.adj_list[u] = []
            if v not in self.adj_list:
                self.adj_list[v] = []

            # Since this is an undirected graph, add v to u's list and u to v's list
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if u not in self.adj_list[v]:
                self.adj_list[v].append(u)

    def get_adj_list(self):
        # Print the adjacency list in a readable format
        for node in self.adj_list:
            print(f"{node} -> {self.adj_list[node]}")
        print("")  # Print a blank line for better spacing

    def bfs(self, start):
        result = []            # List to store the BFS traversal order
        visited = {start}      # Set to keep track of visited nodes
        queue = [start]        # Queue to process nodes in BFS order

        while queue:
            u = queue.pop(0)   # Dequeue the next node
            result.append(u)   # Add it to the result list

            # Visit all unvisited neighbors of u
            for v in self.adj_list[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)

        return result

# Example usage
edges = [["A", "B"], ["A", "E"], ["B", "C"], ["B", "E"], ["C", "D"], ["D", "E"]]
graph = Graph(edges)
graph.get_adj_list()         # Print the graph's adjacency list
print(graph.bfs("A"))        # Perform BFS starting from node "A"
