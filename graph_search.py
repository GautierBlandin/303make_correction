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
    return order[1:]


def bfs_with_top_order(start: int, graph: list[list[int]]) -> list[int]:
    """
    Execute a BFS traversal of the graph, while respecting the topological ordering of the graph.
    Args:
        start: The node to start the search from.
        graph: The graph to search, represented as an adjacency list.
    Returns:
        A list of visited nodes, in topological order and BFS order.
    """
    # Find the in-degree of accessible nodes in the sub-graph.
    n = len(graph)
    in_degree = [0] * n

    q = queue.Queue()
    visited = [False] * n

    q.put(start)
    visited[start] = True

    while not q.empty():
        node = q.get()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                q.put(child)
            in_degree[child] += 1

    # Go through the graph again while respecting topological order.
    order = []

    q = queue.Queue()
    q.put(start)

    while not q.empty():
        node = q.get()
        order.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                q.put(child)

    return order[1:]


