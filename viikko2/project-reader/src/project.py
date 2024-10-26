class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _stringify_list(self, l):
        return "\n- ".join(l) #if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n"
            f"\nAuthors: \n- {self._stringify_list(self.authors)}"
            f"\n"
            f"\nDependencies: \n- {self._stringify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n- {self._stringify_list(self.dev_dependencies)}"
        )
