import parsing
import graph_generation
import printing
import graph_search
import graph_format_conversion


def execute_part_1(filename):
    """
    Execute part 1 of the project: Generate the graph of the Makefile, print the adjacency matrix and all possible paths
    Args:
        filename: Makefile to parse
    """
    content = parsing.read_file(filename)
    dependencies_dict = parsing.parse_file(content)
    adjacency_matrix, name_to_index, index_to_name = graph_generation.generate_graph(dependencies_dict)
    adjacency_list = graph_format_conversion.adjacency_matrix_to_adjacency_list(adjacency_matrix)
    printing.print_adjacency_matrix(adjacency_matrix)
    print()

    for index in range(len(adjacency_matrix)):
        paths = graph_search.find_all_paths(index, adjacency_list)
        for path in paths:
            printing.print_path(path, index_to_name)
