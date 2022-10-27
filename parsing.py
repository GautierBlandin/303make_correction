def read_file(filename) -> str:
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        exit(84)


def parse_file(file_content: str):
    """
    Parse the file content and return the dependency graph
    Args:
        file_content: Contents of the file
    """
    lines = file_content.splitlines()
    lines = [line for line in lines if line != '']

    for i in range(len(lines) // 2):
        rule_line = lines[i * 2]
        command_line = lines[i * 2 + 1]


def parse_rule(rule_line: str) -> tuple[str, list[str]]:
    """
    Parse the rule line
    Args:
        rule_line: Rule line
    Returns:
        (rule name, dependencies)
    """
    rule, dependencies = rule_line.split(":")
    dependencies = [dependency for dependency in dependencies.split(" ")]
    return rule, dependencies
