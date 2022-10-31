import graph_generation
from dependency import Dependency


def test_graph_generation():
    d1c = Dependency(name="d1.c", dep_type="file")
    d1o = Dependency(name="d1.o", dep_type="rule", dependencies=["d1.c"], command="gcc -c d1.c -o d1.o")
    d2c = Dependency(name="d2.c", dep_type="file")
    d2o = Dependency(name="d2.o", dep_type="rule", dependencies=["d1.o", "d2.c"], command="gcc -c d2.c -o d2.o")

    deps = {
        "d1.c": d1c,
        "d1.o": d1o,
        "d2.c": d2c,
        "d2.o": d2o
    }

    graph, name_to_index, index_to_name = graph_generation.generate_graph(deps)

    assert graph == [[0, 1, 0, 0],
                     [0, 0, 0, 1],
                     [0, 0, 0, 1],
                     [0, 0, 0, 0]]

    assert index_to_name == {
        0: "d1.c",
        1: "d1.o",
        2: "d2.c",
        3: "d2.o"
    }

    assert name_to_index == {
        "d1.c": 0,
        "d1.o": 1,
        "d2.c": 2,
        "d2.o": 3
    }
