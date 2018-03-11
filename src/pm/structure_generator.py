import os
import os.path

class Logger(object):
    """Simple logger class."""

    def __init__(self, debug):
        self.debug = debug

    def log(self, message):
        """Prints the message to stdout."""
        if self.debug:
            print(message)


class StructureGenerator(object):
    """Generates folder structures."""

    def __init__(self, logger):
        self.logger = logger

    def __log(self, message):
        if self.logger:
            self.logger.log(message)

    def generate_structure(self, startfrom, structure):
        """Generates folder structure."""
        base_path = startfrom
        dir_separator = "/"
        if not os.path.exists(base_path):
            try:
                os.mkdir(base_path)
            except EnvironmentError:
                self.__log("The startfrom (" + base_path + ") path does not exist and could not be created!")
                raise FileExistsError("Base path does not exist and could not be created (" + base_path + ")!")

        for item in structure:
            if not base_path.endswith(dir_separator) and not item.startswith(dir_separator):
                path = base_path + dir_separator
            else:
                path = base_path
            path = path + item
            if not os.path.exists(path):
                self.__log("Generating path: " + path)
                os.makedirs(path)

    def list_files(self,startpath):
        """Pretty prints the directory structure"""
        for root, dirs, files in os.walk(startpath):
            level = root.replace(startpath, '').count(os.sep)
            indent = '-' * 2 * (level)
            print('{}{}'.format(indent, os.path.basename(root)))
            subindent = '-' * 2 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))

    def list_projects(self,base_path):
        print 'Listing the projects...'
        for items in os.listdir(base_path):
            print items