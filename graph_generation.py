from dependency import Dependency


def generate_graph(dependencies: dict[str, Dependency]) -> tuple[list[list[int]], dict[str, int], dict[int, str]]:
    """
    Generate the graph from the dependency dict
    Args:
        dependencies: Dependency dict
    Returns:
        (adjacency matrix, name to index, index to name)
    """
    graph = []
    name_to_index = {}
    index_to_name = {}

    for index, dependency in enumerate(dependencies.keys()):
        name_to_index[dependency] = index
        index_to_name[index] = dependency
        graph.append([0] * len(dependencies))

    for dependency in dependencies.values():
        if dependency.dep_type == "rule":
            for dep in dependency.dependencies:
                graph[name_to_index[dep]][name_to_index[dependency.name]] = 1

    return graph, name_to_index, index_to_name
