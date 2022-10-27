def adjacency_matrix_to_adjacency_list(graph: list[list[int]]) -> list[list[int]]:
    """
    Convert the adjacency matrix to adjacency list
    Args:
        graph: Adjacency matrix
    Returns:
        Adjacency list
    """
    adjacency_list = []
    for index, line in enumerate(graph):
        adjacency_list.append([])
        for index2, value in enumerate(line):
            if value == 1:
                adjacency_list[index].append(index2)
    return adjacency_list
