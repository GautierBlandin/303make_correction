import queue
from typing import Callable


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


def bfs(start: int, graph: list[list[int]], callback: Callable[[int], None]):
    """
    Traverse the graph with a BFS, and call the callback function on each node.
    Args:
        start: The node to start the search from.
        graph: The graph to search, represented as an adjacency list.
        callback: The function to call on each node.
    """
    n = len(graph)
    visited = [False] * n
    q = queue.Queue()
    q.put(start)

    while q:
        node = q.get()
        callback(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                q.put(child)
