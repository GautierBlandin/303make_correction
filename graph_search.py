def recursive_dfs(start: int, graph: list[list[int]]):
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
