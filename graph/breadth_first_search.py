"""Breadth first search implemented in python."""

from collections import deque


def bfs(graph, start_from, searchable):
    """
    Search for the shortest way of graph using deque.

    :param list graph: List of lists(adjacency matrix), that represents the graph.
    :param int start_from: Starting vertex. Search runs from here.
    :param int searchable: The vertex that needs to be found.

    :returns: String message with found way or message about absence of such way.
    """
    parents = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    search_queue = deque([start_from])

    is_visited[start_from] = True
    while len(search_queue) > 0:
        current_vertex = search_queue.pop()
        if current_vertex == searchable:
            break
        for i, vertex in enumerate(graph[current_vertex]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parents[i] = current_vertex
                search_queue.appendleft(i)
    else:
        return f"There is no way to reach {searchable} from the vertex {start_from}"

    cost_of_way = 0
    way = deque([searchable])
    end_vertex = searchable  # to go from the end to the start

    while parents[end_vertex] != start_from:
        cost_of_way += 1
        way.appendleft(parents[end_vertex])
        end_vertex = parents[end_vertex]

    cost_of_way += 1
    way.appendleft(start_from)

    return (
        f"The shortest way from {start_from} to the {searchable}: {list(way)} has the length"
        f" {cost_of_way}"
    )


# Testing

our_graph = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

print(bfs(our_graph, start_from=1, searchable=3))
