import graph_search


def test_find_all_paths():
    graph = [
        [1, 2],
        [3, 4],
        [3],
        [],
        []
    ]

    paths = graph_search.find_all_paths(0, graph)
    assert paths == [[0, 1, 3], [0, 1, 4], [0, 2, 3]]

    paths = graph_search.find_all_paths(1, graph)
    assert paths == [[1, 3], [1, 4]]

    paths = graph_search.find_all_paths(2, graph)
    assert paths == [[2, 3]]


def test_bfs_order():
    graph = [
        [1, 2],
        [3, 4],
        [3],
        [],
        []
    ]

    order = graph_search.bfs_order(0, graph)
    assert order == [0, 1, 2, 3, 4]

    graph = [
        [1, 3],
        [2],
        [],
        [4],
        [2],
    ]
    order = graph_search.bfs_order(0, graph)
    assert order == [0, 1, 3, 2, 4]


def test_bfs_with_top_order():
    graph = [
        [1, 3],
        [2],
        [],
        [4],
        [2]
    ]

    order = graph_search.bfs_with_top_order(0, graph)
    assert order == [0, 1, 3, 4, 2]
