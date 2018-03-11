import sys
import os
from app import App
from option_parser import CommandLineOptionParser
from options import *

def main():
    """The main function of the application."""
    file_option = FileOption()
    output_option = ProjectPathOption()
    type_option = ProjectTypeOption()
    help_option = HelpOption()
    options = [file_option, output_option,type_option,help_option]
    arg_parser = CommandLineOptionParser(options, "", "")
    arg_parser.parseArguments(sys.argv)

    base_path = ""
    file_path = ""

    """Printing the help option"""
    if arg_parser.help:
        print "Usage: pm [options] SUBCMD [Name]"
        print "Arguments: SUBCMD - The subcommand to execute(list,create,delete,describe) "
        print "           Name   - The name of the project to create,delete or run types on"
        print "Options:"
        print "-h --help            - Show help message"
        print "-t TYPE, --type TYPE - The type of the project created from a specific template"
        print "-p PATH, --path PATH - The base path of the project in whihc to create the project.If not supplied,it uses a default project path from PROJMAN_LOCATION"
        print "Subcommands:"
        print "list     - list the projects which have been created"
        print "create   - Create a new project in PROJMAN_LOCATION"
        print "delete   - Delete an existing project"
        #print "types    - List the types of projects which may be created"
        print "describe - Pretty print the structure of a project"
        sys.exit()

    """checking for project creation directory"""
    if arg_parser.path:
        base_path = arg_parser.path
    if not base_path:
        base_path = os.environ['PROJMAN_LOCATION']
    if not base_path:
        base_path = os.getcwd()

    """checking for the location of yaml file"""
    if arg_parser.file:
        file_path = arg_parser.file
    if not file_path:
        file_path = os.environ['PROJMAN_TEMPLATE']
    app = App(file_path, base_path)

    try:
        if arg_parser.args[1].lower() == 'create' :
            app.run()
        elif arg_parser.args[1].lower() == 'describe':
            app.printStruct()
        elif arg_parser.args[1].lower() == 'list':
            app.listProjects()
        elif arg_parser.args[1].lower() == 'delete':
            print 'Deleting the project...'
        else:
            print "Invalid command provided. Provide one of the subcommand option - create,delete,list,describe"
    except IndexError:
        print "Subcommand missing.Provide one of the subcommand option - create,delete,list,describe"

if __name__ == '__main__':
    main()
