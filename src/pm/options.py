class Option(object):

    def __init__(self, shortname, longname, dest, help_text):
        self.short = shortname
        self.long = longname
        self.dest = dest
        self.help = help_text


class ProjectTypeOption(object):
    """Default project type option."""

    def __init__(self):
        self.short = "-t"
        self.long = "--type"
        self.dest = "type"
        self.help = "The type of the project created from a specific template."


class ProjectPathOption(object):
    """Default project path option."""

    def __init__(self):
        self.short = "-p"
        self.long = "--path"
        self.dest = "path"
        self.help = "The base path in which to create the project."


class FileOption(object):
    """Default yaml file option."""

    def __init__(self):
        self.short = "-f"
        self.long = "--file"
        self.dest = "file"
        self.help = "Path to yaml file."

class HelpOption(object):
    """Default project type option."""

    def __init__(self):
        self.short = "-h"
        self.long = "--help"
        self.dest = "help"
        self.help = "Show help messages."