def recursive_dfs(start: int, graph: list[list[int]]):
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
