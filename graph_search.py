import queue


def find_all_paths(start: int, graph: list[list[int]]):
    """
    Traverse the graph with a DFS, and return all compete paths from the start node.
    Args:
        start: The node to start the search from.
        graph: The graph to search, represented as an adjacency list.
    Returns:
        A list of paths, where each path is a list of nodes.
    """
    paths = []
    order = []

    def rec(node: int):
        order.append(node)
        if len(graph[node]) == 0:
            paths.append(order[:])
        for child in graph[node]:
            rec(child)
        order.pop()

    rec(start)
    return paths


def bfs_order(start: int, graph: list[list[int]]):
    """
    Traverse the graph with a BFS, and call the callback function on each node.
    Args:
        start: The node to start the search from.
        graph: The graph to search, represented as an adjacency list.
    """
    n = len(graph)
    visited = [False] * n
    order = []
    q = queue.Queue()
    q.put(start)

    while not q.empty():
        node = q.get()
        order.append(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                q.put(child)
    return order
