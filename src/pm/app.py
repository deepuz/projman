#!/usr/bin/python
""""""
import os
from structure_generator import StructureGenerator
from structure_config import StructureConfig

class App(object):
    """The main class of the file structure generator tool."""

    def __init__(self, conf_path, base_path, logger=None):
        """Setup the application"""
        self.conf = StructureConfig(conf_path)
        self.base_path = base_path
        self.generator = StructureGenerator(logger)

    def run(self):
        """The application initialization script"""
        self.generator.generate_structure(self.base_path, self.conf.get_paths())

    def printStruct(self):
        self.generator.list_files(self.base_path)

    def listProjects(self):
        self.generator.list_projects(self.base_path)
