class Dependency:
    def __init__(self, name, dep_type, dependencies, command=None):
        self.name = name
        self.dep_type = dep_type
        self.dependencies = dependencies
        self.command = command

    def __str__(self):
        return f"Name: {self.name}, Type: {self.dep_type}, Dependencies: {self.dependencies}, Command: {self.command}\n"

    def __repr__(self):
        return self.__str__()
