class Dependency:
    def __init__(self, name, dep_type, dependencies, command=None):
        self.name = name
        self.dep_type = dep_type
        self.dependencies = dependencies
        self.command = command
