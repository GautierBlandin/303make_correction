from dependency import Dependency


def read_file(filename) -> str:
    """
    Read the file and return its content
    Args:
        filename: File to read
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f'File {filename} not found')
        exit(84)


def parse_file(file_content: str) -> dict[str, Dependency]:
    """
    Parse the file content and return the dependency graph
    Args:
        file_content: Contents of the file
    """
    lines = file_content.splitlines()
    lines = [line for line in lines if line != '']
    dependencies = {}

    for i in range(len(lines) // 2):
        rule_line = lines[i * 2]
        rule_name, deps = parse_rule(rule_line)
        deps = sorted(deps)
        command_line = lines[i * 2 + 1]
        dependencies[rule_name] = (Dependency(name=rule_name, dep_type="rule", dependencies=deps, command=command_line))
        for dep in deps:
            if dep not in dependencies:
                dependencies[dep] = (Dependency(name=dep, dep_type="file"))
    return dict(sorted(dependencies.items()))


def parse_rule(rule_line: str) -> tuple[str, list[str]]:
    """
    Parse the rule line
    Args:
        rule_line: Rule line
    Returns:
        (rule name, dependencies)
    """
    rule, dependencies = rule_line.split(":")
    dependencies = [dependency for dependency in dependencies.split(" ") if dependency != '']
    return rule, dependencies
