import sys
import getopt
import logger

path = None
path_model = None

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.__parseArgs("hm:" + optspec)

    def __parseArgs(self, optspec):
        global  path, path_model

        try:
            opts, args = getopt.getopt(sys.argv[1:], optspec)
        except getopt.GetoptError:
            logger.error("invalid option")
            self.usage()
            exit(1)

        for o, a in opts:
            if o == '-h':
                self.usage()
                exit(0)
            elif o == '-m':
                path_model = a
            else:
                self.handleOpt(o, a)
        if len(args) < 1:
            return False

        path = args[0]
        return True

    def handleOpt(self, o, a):
        pass
