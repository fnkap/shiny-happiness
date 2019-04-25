# Create a dictionary that represents a graph

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 3), ("D", 2), ("E", 3)],
    "C": [("B", 1), ("D", 4), ("E", 5)],
    "D": [],
    "E": [("D", 1)]
}

# Create a list of unvisited nodes

unvisited_nodes = [node for node in graph]

# Let's pick a starting node

starting_node = "A"

# Create a dictionary that keeps track of distances

distances = {}
prev = {}
for node in graph:
    distances[node] = None
    prev[node] = None

# Set the distance of the starting node from itself to zero

distances[starting_node] = 0

# Define the current node as the starting one

current_node = starting_node

while unvisited_nodes:
    unvisited_nodes.remove(current_node)  # Remove the node from the list of unvisited nodes
    for node, distance in graph[current_node]:  # Update distances
        if distances[node] is None:  # If the node is still not visited, update the distance
            distances[node] = distances[current_node] + distance
            prev[node] = current_node
            continue
        if distances[current_node] + distance < distances[node]:  # If we found a shorter path, update the distance
            distances[node] = distances[current_node] + distance
            prev[node] = current_node

    # Find the unvisited node with minimum distance
    current_node = min(distances.items(),
                       key=lambda x: x[1] if (x[1] is not None) and (x[0] in unvisited_nodes) else float("inf"))[0]
# Print the output
print(distances)
print(prev)
