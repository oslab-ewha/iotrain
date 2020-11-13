import sys
import getopt
import logger

path = None
path_model = None
model_type = 'ff'
clearModel = False

class Conf:
    def __init__(self, optspec, usage):
        self.usage = usage
        self.__parseArgs("hm:t:" + optspec)

    def __parseArgs(self, optspec):
        global  path, path_model, model_type

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
            elif o == '-t':
                model_type = a
            else:
                self.handleOpt(o, a)
        if len(args) < 1:
            return False

        path = args[0]
        return True

    def handleOpt(self, o, a):
        pass
