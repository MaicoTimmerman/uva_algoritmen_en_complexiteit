import networkx as nx
on = __import__("1")

def find_most_vital_edge(inputgraph, shortest_path):
    """
    Find the most vital edge, using Dijkstra's algorithm.
    Returns the tuple of vertex of the edge, the shortest path without the vital edge
    and the length of said path.
    """
    most_vital_edge = None
    most_vital_path = None
    longest_shortest_path_length = len(shortest_path)

    # For every edge in the shortest path, remove it and calculate the shortest path again
    # Remember the longest shortest path
    for i in range(0, len(shortest_path) - 1):

        weight = inputgraph.get_edge_data(shortest_path[i], shortest_path[i+1])['weight']
        inputgraph.remove_edge(shortest_path[i], shortest_path[i+1])

        vital_path = nx.dijkstra_path(inputgraph, 0, 14)
        vital_path_length = on.calculate_path_length(inputgraph, vital_path)

        # If the current path is longer than any of the previous, replace its data.
        if (vital_path_length > longest_shortest_path_length):
            most_vital_edge = (shortest_path[i], shortest_path[i+1])
            most_vital_path = vital_path
            longest_shortest_path_length = vital_path_length

        inputgraph.add_edge(shortest_path[i], shortest_path[i+1], weight=weight)

    return most_vital_edge, most_vital_path, longest_shortest_path_length


inputgraph_dict = on.adjmat_to_graph_dict("inputgraph")
inputgraph = on.generate_graph(inputgraph_dict)

print "Dijkstra's algorithm:"
shortest_path = nx.dijkstra_path(inputgraph, 0, 14)
print shortest_path
print on.calculate_path_length(inputgraph, shortest_path)

print('\nMost Vital edge')
print(find_most_vital_edge(inputgraph, shortest_path))
