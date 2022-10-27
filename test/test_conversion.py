import graph_format_conversion


def test_adjacency_matrix_to_adjacency_list():
    graph = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0]
    ]

    adjacency_list = graph_format_conversion.adjacency_matrix_to_adjacency_list(graph)
    assert adjacency_list == [[2], [2, 5], [3], [], [5], [3]]
