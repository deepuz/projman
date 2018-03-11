from optparse import OptionParser


class CommandLineOptionParser(object):
    """
    Command-line parser for the project manager options.
    """

    def __init__(self, options, usage, version):
        self.parser = OptionParser(usage=usage,
                                   version=version,add_help_option=False)
        for option in options:
            self.parser.add_option(option.short, option.long,
                               dest=option.dest, help=option.help)
        self.input_options = options

    def parseArguments(self, args):
        if args[1] == '-h' or args[1] == '--help':
            args.append(" ")
        (options, args) = self.parser.parse_args(args)
        for option in self.input_options:
            attr = getattr(options, option.dest)
            if attr is not None:
                setattr(self, option.dest, attr)
            else:
                setattr(self, option.dest, None)

        self.args = args
        self.options = options