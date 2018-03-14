""""""
import yaml

class ProjectManagerConfig(object):
    """Holds structure configuration nodes."""

    def __init__(self, conf_path):
        with open(conf_path, 'r') as stream:
            data = yaml.load(stream)
            self.nodes = []
            self.permissions = {}
            self.permissionValue = ""
            for x in data:
                self.permissionValue = x.get('permission')
                val = x.get('value')
                #permissions[val] = perm
                self.nodes.append(val)
        self.depth_limit = 5

    def __load(self, conf_path):
        with open(conf_path, 'r') as stream:
            data = yaml.load(stream)
        return [x for x in data]

    def get_paths(self, type):
        """Get the node paths as a list."""
        paths_list = []
        node = []
        for item in self.nodes:
            if type in item:
                node = item.get(type)
                break
        self.__get_paths(paths_list, node, 0, "/")
        return paths_list

    def __get_paths(self, output, nodes, depth, parent):
        try:
            if isinstance(nodes, dict):
                for key, value in nodes.items():
                    if key == "permission":
                        self.permissionValue = value
                    else:
                        path = self.__create_path_string(parent, value)
                        if not path == "/":
                            output.append(path)
                        if isinstance(value, str):
                            self.permissions[value] = self.permissionValue
                        elif isinstance(value, list):
                            self.__get_paths(output, value, depth + 1, path)
                        elif isinstance(value,dict):
                            for innerKey,innerValue in value.items():
                                path = self.__create_path_string(parent,innerKey)
                                self.__get_paths(output, innerValue, depth, path)
                return
            elif isinstance(nodes, list):
                for item in nodes:
                    if isinstance(item, list) or isinstance(item, dict):
                        self.__get_paths(output, item, depth+1, parent)
        except ValueError:
            print "Value error"


    def __create_path_string(self, parent, child):
        if not isinstance(child,str):
            return parent
        if parent == "":
            path = "/" + child
        elif parent == "/":
            path = parent + child
        else:
            path = parent + "/" + child
        return path



