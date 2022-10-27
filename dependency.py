class Dependency:
    """
    Dependency class
    Attributes:
        name: Name of the dependency
        dep_type: Type of the dependency (file or rule)
        dependencies: List of dependencies (only for rule)
        command: Command to execute (only for rule)
    """
    def __init__(self, name, dep_type, dependencies=None, command=None):
        self.name = name
        self.dep_type = dep_type
        self.dependencies = dependencies
        self.command = command

    def __str__(self):
        return f"Name: {self.name}, Type: {self.dep_type}, Dependencies: {self.dependencies}, Command: {self.command}\n"

    def __repr__(self):
        return self.__str__()
