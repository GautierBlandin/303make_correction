import parsing
import graph_generation
import printing
import graph_search
import graph_format_conversion


def execute_part_2(filename: str, dep: str):
    """
    Execute part 2 of the project: Compute the commands needed to be executed to build the target
    Args:
        filename: Makefile to parse
        dep: Modified file
    """
    content = parsing.read_file(filename)
    dependencies_dict = parsing.parse_file(content)
    adjacency_matrix, name_to_index, index_to_name = graph_generation.generate_graph(dependencies_dict)
    adjacency_list = graph_format_conversion.adjacency_matrix_to_adjacency_list(adjacency_matrix)

    if dep not in name_to_index:
        exit(84)
    dep_index = name_to_index[dep]
    order = graph_search.bfs_order(dep_index, adjacency_list)
    printing.print_command_order(order, index_to_name, dependencies_dict)
