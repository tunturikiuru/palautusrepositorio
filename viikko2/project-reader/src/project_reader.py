from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        content_dict = toml.loads(content)

        name = content_dict['tool']['poetry']['name']
        description = content_dict['tool']['poetry']['description']
        dependencies = list(content_dict['tool']['poetry']['dependencies'].keys())
        dev_dependencies = list(content_dict['tool']['poetry']['group']['dev']['dependencies'].keys())
        license = content_dict['tool']['poetry']['license']
        authors = list(content_dict['tool']['poetry']['authors'])

        project = Project(name, description, dependencies, dev_dependencies, license, authors)
        return project
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
