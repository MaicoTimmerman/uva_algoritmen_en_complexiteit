import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def adjmat_to_graph_dict(filename):
    """
    Convert adjacency matrix stored in plain text file to a dict representing
    the graph in the following way:

    graph_dict = {'V0': [(Vx, weight), ... (Vx, weight)],
                  'V1': [(Vx, weight), ... (Vx, weight)],
                  ...
                  'Vn': [(Vx, weight), ... (Vx, weight)]}

    Where the keys V0-Vn represent every vertex in the graph, and the value
    array contains the outgoing edges as as (destination vertex, edge weight)
    tuple
    """

    f = open(filename, 'r')
    lines = f.readlines()
    graph = {}

    current_vertex = 0

    # Each line in the file represents the outgoing edges from a vertex
    for vertex in lines:

        current_edge = 0

        # Iterate through all possible edges
        for weight in vertex.split():

            # Add edge tuple to appropriate dict entry if vertices are connected
            if int(weight) != -1:
                if current_vertex in graph:
                    graph[current_vertex].append((current_edge,int(weight)))
                else:
                    graph[current_vertex] = [(current_edge,int(weight))]

            current_edge += 1

        current_vertex += 1

    return graph


def generate_graph(graph_dict):
    """
    Converts graph in dict format to NetworkX directed weighted graph
    """

    graph = nx.DiGraph()

    # No need to add vertices beforehand
    for vertex in graph_dict:
        for edge in graph_dict[vertex]:
            graph.add_edge(vertex, edge[0], weight=edge[1])

    return graph


def calculate_path_length(graph, path):
    """
    Returns the length of weighted graph path (NetworkX)
    """

    length = 0

    for i in range(0, len(path) - 1):
        length += graph.get_edge_data(path[i], path[i+1])['weight']

    return length


def shortest_path_in_list(graph, paths):
    """
    Returns the shortest path in a list of paths (NetworkX)
    """

    # Initially set the first path to be the shortest
    shortest_path = paths[0]
    shortest_path_length = calculate_path_length(graph, shortest_path)

    for path in paths:
        length = calculate_path_length(graph, path)
        if length < shortest_path_length:
            shortest_path = path
            shortest_path_length = length

    return shortest_path

if __name__ == "__main__":
    # Load file
    inputgraph_dict = adjmat_to_graph_dict("inputgraph")
    inputgraph = generate_graph(inputgraph_dict)

    # Determine shortest path by examining all paths between the two points, the
    # naive algorithm
    print "Naive algorithm:"
    shortest_path = shortest_path_in_list(inputgraph, list(nx.all_simple_paths(inputgraph, 0, 14)))
    print shortest_path
    print calculate_path_length(inputgraph, shortest_path)

    # Determine shortest path using Dijksta's algorithm
    print "\nDijkstra's algorithm:"
    shortest_path = nx.dijkstra_path(inputgraph, 0, 14)
    print shortest_path
    print calculate_path_length(inputgraph, shortest_path)
