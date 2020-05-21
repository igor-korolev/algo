"""Dijkstra's algorithm of finding the shortest paths between vertexes in a graph."""


def dijkstra_path(graph, start):
    """
    Find the shortest paths between nodes using dijkstra algorithm.

    :param list graph: List of lists(adjacency matrix), that represents the graph.
    :param int start: Starting vertex. Search runs from here.

    :returns: List with the shortest paths to all possible nodes from the provided start.
    """
    graph_length = len(graph)
    is_visited = [False] * graph_length
    cost = [float("inf")] * graph_length

    cost[start] = 0  # We already in starting position, so the cost is zero
    min_cost = 0  # This will show us whether we move on by graph or not

    while min_cost < float("inf"):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
        min_cost = float("inf")
        for vertex_index in range(graph_length):
            if min_cost > cost[vertex_index] and not is_visited[vertex_index]:
                min_cost = cost[vertex_index]
                start = vertex_index
    return cost


# Testing

graph_for_test = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

print(dijkstra_path(graph_for_test, 7))
