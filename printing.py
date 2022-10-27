from dependency import Dependency


def print_adjacency_matrix(graph: list[list[int]]) -> None:
    """
    Print the adjacency matrix with expected format
    Args:
        graph: Adjacency matrix
    """
    for line in graph:
        line_string = "["
        for value in line:
            line_string += f"{value} "
        line_string = line_string[:-1]
        line_string += "]"
        print(line_string)


def print_path(path: list[int], index_to_name: dict[int, str]) -> None:
    """
    Print the path with expected format
    Args:
        path: Path to print
        index_to_name: Index to name dict
    """
    if len(path) == 1:
        return
    path_string = ""
    for index in path:
        path_string += f"{index_to_name[index]} -> "
    path_string = path_string[:-4]
    print(path_string)


def print_command_order(order: list[int], index_to_name: dict[int, str], dependencies_dict: dict[str, Dependency]) -> None:
    """
    Print the command order with expected format
    Args:
        order: Command order
        index_to_name: Index to name dict
        dependencies_dict: Dependency dict
    """
    commands = []
    for index in order:
        name = index_to_name[index]
        if dependencies_dict[name].dep_type == "rule":
            commands.append(dependencies_dict[name].command)
    if len(commands) == 0:
        print("")
    else:
        for command in commands:
            print(command)
