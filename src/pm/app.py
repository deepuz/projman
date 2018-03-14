import os
from project_structure_generator import ProjectStructureGenerator
from projman_config import ProjectManagerConfig

class App(object):
    """The main class of the file structure generator tool."""

    def __init__(self, conf_path, base_path, logger=None):
        """Setup the application"""
        self.conf = ProjectManagerConfig(conf_path)
        self.base_path = base_path
        self.generator = ProjectStructureGenerator(logger)

    def run(self,type, projectName):
        """The application initialization script"""
        self.generator.generate_structure(self.base_path, self.conf.get_paths(type), projectName)

    def printStruct(self):
        self.generator.list_files(self.base_path)

    def listProjects(self):
        self.generator.list_projects(self.base_path)
